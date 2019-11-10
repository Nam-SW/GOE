# import tensorflow as tf
# import numpy as np


# load_data = np.load('./dataset/m1_input.npy')
# print(load_data)

import datetime
def get_day(day):
    day_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_code = ['월', '화', '수', '목', '금', '토', '일']

    month = 1
    for i in day_len:
        if day > i:
            month += 1
            day -= i
        else:
            break
    print(month, day)
    return day_code[datetime.date(2018, month, day).weekday()]


while True:
    print(get_day(int(input())))