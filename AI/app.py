from flask import Flask, request, jsonify
# import requests
from GOE_AI import GOE
import firebase_admin
from firebase_admin import credentials, db
import threading
import time

app = Flask(__name__)
goe = GOE()
DB_link='https://guardians-of-energy.firebaseio.com/'
DB_cred='./GOE.json'

firebase_admin.initialize_app(credentials.Certificate(DB_cred), {
    'databaseURL' : DB_link
})

@app.route('/')
def wrong_access():
    try:
        return jsonify({'message':'잘못된 접근입니다'})
    except Exception as e:
        print(str(e))
        return jsonify({'message':str(e)})

@app.route('/reloading')
def get_predict():
    try:
        year = goe.get_today()[:4]
        d = list(map(lambda data: [data['Month'], data['Day'], data['Temperature'], data['Weather']], [db.reference(year+'/weather/'+key).get() for key in goe.remaining_day()]))
        # print(d)
        pred = goe.predict(d)
        data_json = {k:v for k,v in enumerate(pred)}
        return data_json, 200
    except Exception as e:
        print(str(e))
        return jsonify({'message':str(e)})

def update():
    while True:
        if time.strftime('%H', time.localtime(time.time())) == '00':
        # if True:
            yesterday = goe.get_yesterday_weather()
            db.reference(yesterday[0][:4]+'/weather').child(yesterday[0][4:]).set({
                'Month': yesterday[1], 
                'Day': yesterday[2], 
                'Temperature': yesterday[3],
                'Weather': yesterday[4]
            })
            print('이전날 변경 완료')

            ref = db.reference(goe.get_today()[:4]+'/weather')
            for key, data in zip(goe.remaining_day(), goe.weather_predict()): # 이번달 예측
                # print(key, data)
                d_ref = ref.child(key)
                d_ref.set({
                    'Month': data[0],
                    'Day': data[1],
                    'Temperature': data[2],
                    'Weather': data[3]
                })

            data = db.reference(yesterday[0][:4]+'/electricity_use/'+yesterday[0][4:]).get()
            x = yesterday[1:3] + yesterday[3:]
            y = [data[i]['airconditioner'] for i in data.keys()] + [data[i]['refrigerator'] for i in data.keys()]
            print(x)
            print(y)

            # goe.weather_predict()
        time.sleep(3600)

if __name__ == '__main__':
    threading.Thread(target=update).start()
    app.run(host='0.0.0.0', debug=True, port=8080)
    
    