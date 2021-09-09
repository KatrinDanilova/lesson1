weather = {
    'city': 'Москва',
    'temperature': 20,
    'wind': 'восточный'
}
print(weather)

print(weather['city'])

weather['temperature'] = 30
print(weather)

print(len(weather))

print('country' in weather)
print('country' not in weather)

weather['date'] = '07.09.2021'
print(weather)

#создайте список, добавьте туда 3 словаря с погодой за разные даты при помощи append
list_weather = []
list_weather.append(weather)

weather['temperature'] = 25
weather['date'] = '08.09.2021'
list_weather.append(weather)

weather['temperature'] = 27
weather['date'] = '09.09.2021'
list_weather.append(weather)

print(list_weather)


