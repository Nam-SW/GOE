import time
import numpy as np
from keras.models import load_model
from selenium import webdriver

from weather_data import get_weather_code, get_temperature
from weather_predict import get_predict_code


class GOE:
    def __init__(self, model_link='./model1.h5', 
                 driver_link='C:\\ProgramData\\Anaconda3\\chromedriver.exe'):
        '''
        model_link = AI 모델 링크
        driver_link = 크롬 드라이버 위치
        DB_link = 파베 링크
        '''
        self.model = load_model(model_link)
        self.driver = driver_link
        
    def get_today(self):
        '''
        0:4 = 년 4:6 = 월 6:8 = 일 8 = 요일
        '''
        date = time.strftime('%Y%m%d', time.localtime(time.time())) + str(int(time.strftime('%w', time.localtime(time.time())))+1)
        return date
    
    def get_yesterday_weather(self):
        date = self.get_today()
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:8])
        t = get_temperature(year, month)[day-2] # 하나는 인덱스, 하나는 하루 전
        w = get_weather_code(year, month)[day-2]
        return t, w
        
    def weather_predict(self):
        daylen = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        date = self.get_today()
        month = int(date[4:6])
        today = int(date[6:8])
        return get_predict_code(self.driver, daylen[month-1]-(today-1))
    
    def model_fit(self, x, y):
        x = np.array([x])
        y = np.array([y]) * 10
        self.model.fit(x, y, epochs=1, batch_size=1, validation_split=1, verbose=2)





test = GOE()
# print(test.get_today())
# test.update_yesterday()
print(test.weather_predict())