import numpy as np
from keras.models import load_model
from selenium import webdriver

import weather_predict


class GOE:
    def __init__(self, model_link='./model1.h5', driver_link='C:\\ProgramData\\Anaconda3\\chromedriver.exe', DB_link=''):
        '''
        model_link = AI 모델 링크
        driver_link = 크롬 드라이버 위치
        DB_link = 파베 링크
        '''
        self.m = load_model(model_link)
        self.driver = webdriver.Chrome(driver_link)
        self.DB = DB_link

    def get_today():