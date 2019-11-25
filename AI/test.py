import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from GOE_AI import GOE
from weather_data import get_temperature, get_weather_code, get_day

DB_link='https://guardians-of-energy.firebaseio.com/'
DB_cred='./GOE.json'

firebase_admin.initialize_app(credentials.Certificate(DB_cred), {
    'databaseURL' : DB_link
})

# ref = db.reference()
# print(ref.get())

goe = GOE()
# t, w = get_temperature(2019, 11), get_weather_code(2019, 11) # 11월 데이터 등록
ref = db.reference('2019/weather')
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

# print(goe.weather_predict())
# for key, data in zip(goe.remaining_day(), goe.weather_predict()): # 이번달 예측
#     # print(key, data)
#     d_ref = ref.child(key)
#     d_ref.set({
#         'Month': data[0],
#         'Day': data[1],
#         'Temperature': data[2],
#         'Weather': data[3]
#     })