import time
import numpy as np
from tensorflow.keras.models import load_model

from weather_data import get_weather_code, get_temperature, get_day
from weather_predict import get_predict_code


class GOE:
    def __init__(self, model_link='./models/model.h5', driver_link='C:\\ProgramData\\Anaconda3\\chromedriver.exe'):
        '''
        model_link = AI 모델 링크
        driver_link = 크롬 드라이버 위치
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
        '''
        매일 0시에 실행하는 함수. 
        하루가 지나고 전날의 정확한 데이터를 리스트로 얻어옴.
        [년월일, 월, 요일, 온도, 날씨]
        '''
        date = self.get_today()
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:8])
        t = get_temperature(year, month)[day-2] # 하나는 인덱스, 하나는 하루 전
        w = get_weather_code(year, month)[day-2]

        yesterday = time.strftime('%Y%m%d%w', time.localtime(time.time()-86400)) # 전날 3600 * 24
        return [yesterday[:8], int(yesterday[4:6]), int(yesterday[-1])+1, t, w]


    def weather_predict(self):
        '''
        매일 0시에 실행하는 함수. 현재 달의 모든 날씨 정보를 예측하고 반환. 
        '''
        reday = self.remaining_day()
        year = int(self.get_today()[:4])
        month = int(reday[0][:2])
        restart = 1
        tw = []
        while restart != len(reday):
            temp, restart = get_predict_code(self.driver, restart, len(reday))
            tw += temp
        print(len(tw))
        
        data = []
        for day, t, w in zip(map(lambda x: int(x[2:]), reday), tw[0], tw[1]):
            # print(month, get_day(year, month, day), t, w)
            data.append([month, get_day(year, month, day), t, w])

        return data
    

    def model_fit(self, x, y, link='./models'):
        '''
        매일 0시에 실행하는 함수. 그 전날의 데이터를 가져다가 모델을 학습시키고 저장. 
        원본은 드라이브에 있으니 우선은 상관없음.
        '''
        x = np.array([x])
        y = np.array([y]) * 10
        self.model.fit(x, y, epochs=1, batch_size=1, validation_split=1, verbose=2)
        self.model.save(link+'/model.h5')
    
    
    def predict(self, data):
        '''
        데이터를 주면 그걸 예측해서 데이터 개수만큼 예측값을 줌
        '''
        datalist = [list(map(lambda x:1 if x >= 0.5 else 0, self.model.predict(np.array([i]))[0])) for i in data]
        return datalist


    def remaining_day(self):
        '''
        파베에서 사용할 남은 날짜만큼 폴더 이름 구하기
        '''
        daylen = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        date = self.get_today()
        today = int(date[6:8])
        return [date[4:6]+"%02d"%i for i in range(today, daylen[int(date[4:6])-1]+1)]



if __name__ == '__main__':
    test = GOE()
    # print(test.get_today())
    
    # test.update_yesterday()
    
    # test.weather_predict()
    
    # print(test.remaining_day())
    print(test.get_yesterday_weather())