import requests, re, datetime
from bs4 import BeautifulSoup
# from pprint import pprint

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
    temperature = []

    res = requests.get(get_url(year, month, 1))
    soup = BeautifulSoup(res.content, 'html5lib')
    find = soup.find_all(string=re.compile('평균기온:'))

    for i in find:
        if len(i) <= 5:
            break
        temperature.append(float(i[5:-1]))

    return temperature

def get_day(year, month, day):
    '''
    년월일 입력하면 날짜코드 알려줌
    '''
    day_code = [2, 3, 4, 5, 6, 7, 1]
    return day_code[datetime.date(year, month, day).weekday()]

def get_weather_code(year, month):
    '''
    년도를 받아와서 그 년도의 데이터를 측정함. 
    19년 데이터는 올바르지 않으니 그 이전 데이터를 쓰도록 하자.
    
    햇무리, \xa0
    채운, 연무, 박무, 안개
    비, 소나기, 우박
    눈, 싸락눈, 소낙눈
    진눈깨비
    '''
    weather_list, weather_code = [], []
    
    temp = []
    res = requests.get(get_url(year, month, 2))
    soup = BeautifulSoup(res.content, 'html5lib')
    find = soup.find_all(class_='align_left')

    # 월별로 시작하는 요일
    start = get_day(year, month, 1) + 6
    for j in range(start, len(find)):
        text = find[j].get_text()
        if find[j-7].get_text()[0].isdigit():
            weather_list.append(text)
    

    # 코드화
    for i in weather_list:
        if '진눈깨비' in i:
            # 진눈깨비: 5
            weather_code.append(5)
        elif '눈' in i:
            # 눈: 4
            weather_code.append(4)
        elif '소나기' in i or '비' in i or '우박' in i:
            # 비: 3
            weather_code.append(3)
        elif '무' in i or '운' in i or '안개' in i:
            # 흐림: 2
            weather_code.append(2)
        elif '\xa0' in i or '햇무리' in i:
            # 맑음: 1
            weather_code.append(1)
        else:
            # 아직 코드를 추가하지 않음. 나중에 프로그램이 커지면 알아서 하겠지
            weather_code.append(0)
    
    return weather_code

def get_data(year):
    data_list = []

    weather = get_weather_code(year, 1)
    temperature = get_temperature(year, 1)

    for month in range(len(weather)):
        for day in range(len(weather[month])):
            temp = [month+1, get_day(year, month+1, day+1), temperature[month][day], weather[month][day]]
            # print(temp)
            data_list.append(temp)
    
    # data = np.array(data_list)
    return data_list

if __name__ == "__main__":
    print(len(get_temperature(2019, 11)))
    print(len(get_weather_code(2019, 11)))