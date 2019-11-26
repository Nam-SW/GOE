import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from GOE_AI import GOE
# from weather_data import get_temperature, get_weather_code, get_day

DB_link='https://guardians-of-energy.firebaseio.com/'
DB_cred='./GOE.json'

firebase_admin.initialize_app(credentials.Certificate(DB_cred), {
    'databaseURL' : DB_link
})

# print(db.reference('2019/electricity_use/1100').get())

# ref = db.reference()
# print(ref.get())

# goe = GOE()
# t, w = get_temperature(2019, 11), get_weather_code(2019, 11) # 11월 데이터 등록
# ref = db.reference('2019/weather')
# for d in range(len(t)):
#     k = "11%02d"%(d+1)
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
# x = np.load('./dataset/m1_Xtrain.npy')
# y = np.load('./dataset/m1_Ytrain.npy')

# ref = db.reference('2019/electricity_use')
# for i, k in zip(range(304, 329), range(1, 26)):
#     key = '11%02d'%k
#     print(key)
    
#     test = ref.child(key)

#     test.set({k1:{k2:int(y[i][k1+i2]) for k2, i2 in zip(['airconditioner', 'refrigerator'], [0, 48])} for k1 in range(48)})

import datetime, time
while True:
    now = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    print(now[:4]+'/electricity_use/'+now[4:8] + str(int(now[8:10])*2 + (int(now[10:]) // 30)))
    if now[8:] == '0000':
        db.reference(now[:4]+'/electricity_use').child(now[4:8]).set({})
        print(now + ' : mk table')
    if now[10:] in ['00', '30']:
        key = int(now[8:10])*2 + (int(now[10:]) // 30)
        # print(key)
        db.reference(now[:4]+'/electricity_use/'+now[4:8]).child(key).set({'airconditioner':0, 'refrigerator':1})
        print(now + ' : update')
    time.sleep(60)