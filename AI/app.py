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

# @app.route('/')
# def wrong_access():
#     try:
#         return jsonify({'message':'잘못된 접근입니다'})
#     except Exception as e:
#         print(str(e))
#         return jsonify({'message':str(e)})

@app.route('/')
def get_predict():
    try:
        today = goe.get_today()
        f_count = [0] * 2 # 요 2을 가구 수대로 바꾸기만 하면 됨.
        if today[6:8] != '01':
            data = db.reference(today[:4]+'/electricity_use').get()
            month = today[4:6]
            for day in range(1, int(today[6:8])):
                # print(data[month+'%02d'%day])
                for d in data[month+'%02d'%day]:
                    # print(d)
                    for i, k in enumerate(list(d.keys())):
                        f_count[i] += d[k]

        
        # print(f_count)


        year = goe.get_today()[:4]
        d = list(map(lambda data: [data['Month'], data['Day'], data['Temperature'], data['Weather']], [db.reference(year+'/weather/'+key).get() for key in goe.remaining_day()]))
        # print(d)
        return_value = ''
        pred = goe.predict(d)
        for l in pred:
            for i in range(len(l)//48):
                f_count[i] += sum(l[i*48 : (i+1)*48])
            # print(f_count)
            return_value += ' '.join(map(str, f_count)) + ' '

        # data_json = {k:v for k,v in enumerate(pred)}
        return return_value[:], 200
    except Exception as e:
        print(str(e))
        return jsonify({'message':str(e)})

def update():
    while True:
        if time.strftime('%H', time.localtime(time.time())) == '00':
        # if True:
            yesterday = goe.get_yesterday_weather() # 전날 변경
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
            print('예측 업데이트 완료')


            data = db.reference(yesterday[0][:4]+'/electricity_use/'+yesterday[0][4:]).get() # 모델 학습
            print(data)
            x = yesterday[1:3] + yesterday[3:]
            y = []
            for k in data[0].keys():
                for i in data:
                    y.append(i[k])
                    
            # print(x)
            # print(y)

            goe.model_fit(x, y)
            print('모델 학습 완료')
        time.sleep(3600)

if __name__ == '__main__':
    threading.Thread(target=update).start()
    app.run(host='0.0.0.0', debug=True, port=8080)
    
    