# import dataset.weather_data as wd

# import datetime
# def get_day(day):
#     day_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    

#     month = 1
#     for i in day_len:
#         if day > i:
#             month += 1
#             day -= i
#         else:
#             break
#     return month, day
    


# year = 2018
# data_list = []

# weather = wd.get_weather_code(year)
# temperature = wd.get_temperature(year)

# for month in range(len(weather)):
#     temp = []
#     for day in range(len(weather[month])):
#         t = [month+1, wd.get_day(year, month+1, day+1), temperature[month][day], weather[month][day]]
#         temp.append(t)
#     data_list.append(temp)
# print('준비완료')
# day_code = ['월', '화', '수', '목', '금', '토', '일']
# day_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# while True:
#     i = int(input())
#     month, day = get_day(i)

#     if i == 0:
#         for m in range(9, 12):
#             for d in range(day_len[m-1]):
#                 if data_list[m-1][d-1][-1] == 3:
#                     print(m, d, day_code[datetime.date(2018, m, d).weekday()])
#                     print(data_list[m-1][d-1])
#     else:
#         print(month, day, day_code[datetime.date(2018, month, day).weekday()])
#         print(data_list[month-1][day-1])


import numpy as np
import pandas as pd

try:
    data = pd.read_csv('./dataset/model1_output.csv')
    np.save('./dataset/m1_output.npy', data.to_numpy())
    
except:
    print('파일 불러오기 실패')