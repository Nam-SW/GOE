import weather_data
import numpy as np

if __name__ == "__main__":
    year = 2018
    data_list = []

    weather = weather_data.get_weather_code(year)
    temperature = weather_data.get_temperature(year)

    for month in range(len(weather)):
        for day in range(len(weather[month])):
            temp = [month+1, weather_data.get_day(year, month+1, day+1), temperature[month][day], weather[month][day]]
            # print(temp)
            data_list.append(temp)
    
    data = np.array(data_list)
    np.save('./m1_input', data)

    
    