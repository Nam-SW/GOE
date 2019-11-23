import weather_data
import numpy as np

if __name__ == "__main__":
    year = 2017
    data_list = []

    weather = weather_data.get_weather_code(year)
    temperature = weather_data.get_temperature(year)

    for month in range(len(weather)):
        for day in range(len(weather[month])):
            temp = [month+1, weather_data.get_day(year, month+1, day+1), temperature[month][day], weather[month][day]]
            # print(temp)
            data_list.append(temp)
    
    data = np.array(data_list)
    np.save('./dataset/m1_test', data)



d = np.load('./dataset/m1_test.npy')
idxes = np.random.choice([i for i in range(len(d))], 30, replace=False)
data = np.array([d[i] for i in idxes])
np.save('./dataset/m1_test.npy', data)

