from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:\\ProgramData\\Anaconda3\\chromedriver.exe' # 윈도우 
url = 'https://www.accuweather.com/ko/kr/seoul/226081/daily-weather-forecast/226081?day='
driver = webdriver.Chrome(chromedriver)

temperature_list = []
weather_list = []

for i in range(1, 81):
    driver.get(url + str(i))

    t = driver.find_elements_by_class_name('value')
    w = driver.find_elements_by_class_name('phrase')

    high, low = str(t[0].text), str(t[1].text)
    mean = (int(high[:high.index('°')]) + int(low[:low.index('°')])) / 2
    temperature_list.append(mean)
    weather_list.append((str(w[0].text), str(w[1].text)))

driver.quit()

# pprint(temperature_list)
weather_code = []
for weather in weather_list:
    i = weather[0]
    if '진눈깨비' in i:
        # 진눈깨비: 5
        weather_code.append(5)
    elif '눈' in i:
        # 눈: 4
        weather_code.append(4)
    elif '소나기' in i or '비' in i:
        # 비: 3
        weather_code.append(3)
    elif '흐' in i:
        # 흐림: 2
        weather_code.append(2)
    elif '맑' in i or '줄어듦' in i:
        # 맑음: 1
        weather_code.append(1)
    else:
        # 아직 코드를 추가하지 않음. 나중에 프로그램이 커지면 알아서 하겠지
        weather_code.append(0)
    
print(weather_code)
# pprint(set([i[0] for i in weather_list]))


"""
맑음, 대체로 맑음, 구름이 줄어듦
대체로 흐림, 약간 흐림, 흐림
소나기, 비
눈
진눈깨비
"""