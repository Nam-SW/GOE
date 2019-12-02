import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from GOE_AI import GOE
from weather_data import get_temperature, get_weather_code, get_day
from weather_predict import get_predict_code
import datetime, time

DB_link='https://guardians-of-energy.firebaseio.com/'
DB_cred='./GOE.json'

firebase_admin.initialize_app(credentials.Certificate(DB_cred), {
    'databaseURL' : DB_link
})


goe = GOE()
# t, w = get_temperature(2019, 12), get_weather_code(2019, 12) # 11월 데이터 등록
# ref = db.reference('2019/weather')
# for d in range(len(t)):
#     k = "12%02d"%(d+1)
#     print(d, k)
#     d_ref = ref.child(k)
#     d_ref.set({
#         'Month': 11,
#         'Day': get_day(2019, 11, d+1),
#         'Temperature': t[d],
#         'Weather': w[d]
#     })

# ref = db.reference('2019/weather')
# for key, data in zip(goe.remaining_day(), goe.weather_predict()): # 이번달 예측
#     # print(key, data)
#     d_ref = ref.child(key)
#     d_ref.set({
#         'Month': data[0],
#         'Day': data[1],
#         'Temperature': data[2],
#         'Weather': data[3]
#     })


# import numpy as np
# y = np.load('./dataset/m1_Ytrain.npy')

# ref = db.reference('2019/electricity_use')
# for i, k in zip(range(334, 336), range(1, 31)): # 11월 1일~30일
#     key = '12%02d'%k
#     print(key)
#     test = ref.child(key)
#     test.set({k1:{k2:int(y[i][k1+i2]) for k2, i2 in zip(['airconditioner', 'refrigerator'], [0, 48])} for k1 in range(48)})

ref = db.reference(goe.get_today()[:4]+'/weather')
while True:
    try:
        for key, data in zip(goe.remaining_day(), goe.weather_predict()): # 이번달 예측
            # print(key, data)
            d_ref = ref.child(key)
            d_ref.set({
                'Month': data[0],
                'Day': data[1],
                'Temperature': data[2],
                'Weather': data[3]
                })
        break
    except:
        print('error')








############################################## 여기가 꼭 실행해야하는곳 ##########################################
now = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
for i in range(int(now[8:10])*2 + (int(now[10:]) // 30)+1):
    print(i)
    db.reference(now[:4]+'/electricity_use/'+now[4:8]).child(str(i)).set({'airconditioner':0, 'refrigerator':1})


while True:
    now = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # print(now[:4]+'/electricity_use/'+now[4:8] + str(int(now[8:10])*2 + (int(now[10:]) // 30)))

    if now[8:] == '0000':
        db.reference(now[:4]+'/electricity_use').child(now[4:8]).set({0:{'airconditioner':0, 'refrigerator':1}})
        print(now + ' : mk table')
        time.sleep(60)
        continue
    
    if now[10:] in ['00', '30']:
        key = str(int(now[8:10])*2 + (int(now[10:]) // 30))
        print(now[:4]+'/electricity_use/'+now[4:8]+'/', key)
        db.reference(now[:4]+'/electricity_use/'+now[4:8]).child(key).set({'airconditioner':0, 'refrigerator':1})
        print(now + ' : update')
    time.sleep(60)