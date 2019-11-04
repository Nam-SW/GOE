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

for i in range(1, 51):
    driver.get(url + str(i))

    t = driver.find_elements_by_class_name('value')
    w = driver.find_elements_by_class_name('phrase')

    high, low = str(t[0].text), str(t[1].text)
    mean = (int(high[:high.index('°')]) + int(low[:low.index('°')])) / 2
    temperature_list.append(mean)
    weather_list.append((str(w[0].text), str(w[1].text)))

driver.quit()

pprint(temperature_list)
pprint(weather_list)