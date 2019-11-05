import requests, re, datetime
from bs4 import BeautifulSoup
from pprint import pprint
from konlpy.tag import Twitter

def get_url(year, month, option):
    '''
    옵션은 온도를 원하면 1, 날씨를 원하면 2를 넣어야함.
    '''
    url = 'https://www.weather.go.kr/weather/climate/past_cal.jsp?stn=108&yy=' + str(year) + '&mm=' + str(month)
    if option == 1:
        url += '&obs=1&x=0&y=0'
    else:
        url += '&obs=9&x=0&y=0'
    return url

def get_temperature(year, month):
    '''
    월별로 온도 구하는 함수임
    '''
    temperature = {}

    res = requests.get(get_url(year, month, 1))
    soup = BeautifulSoup(res.content, 'html5lib')
    find = soup.find_all(string=re.compile('평균기온:'))

    for i, j in zip([i+1 for i in range(len(find))], find):
        temperature[i] = float(j[5:-1])

    return temperature

def get_day(year, month, day):
    '''
    년월일 입력하면 날짜코드 알려줌
    '''
    day_code = [2, 3, 4, 5, 6, 7, 1]
    return day_code[datetime.date(year, month, day).weekday()]


def get_weather_list(year):
    '''
    일단 이 함수는 예측된 날씨들이 뭐뭐가 있는지 내가 알기 위해 사용하는거.
    어차피 이런 날씨들은 내가 직접 코드화할거라 프로그래밍에 영향을 끼치진 않음
    단 안되면 내가 페이지 하나하나 방문하면서 뭐뭐있는지 알아야하기 때문에 내가 빡침
    '''
    weather = []
    for i in range(1, 13):
        res = requests.get(get_url(year, i, 2))
        soup = BeautifulSoup(res.content, 'html5lib')

        for i in soup.find_all(class_='align_left'):
            text = i.get_text()
            if text != '\xa0' and not text[0].isdigit():
                weather.append(text)
                # print(text)

    weather = list(set(weather))
    weather_str = ''
    for i in weather:
        weather_str += i
    

    h = Twitter()
    nouns = h.nouns(weather_str)
    return nouns

pprint(set(get_weather_list(2018) + get_weather_list(2017) + get_weather_list(2016)))


"""
햇무리, \xa0
채운, 연무, 박무, 안개
비, 소나기, 우박
눈, 싸락눈, 소낙눈
진눈깨비
"""