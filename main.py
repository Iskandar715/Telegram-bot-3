from countryinfo import CountryInfo
from pprint import pprint
import json


country_data = []
while True:
    country_name = input('Davlat nomini kiriting: ')
    if country_name.lower() == 'stop':
        print('Dastur toxtadi !!!')
        with open('country_info.json', mode='a', encoding='utf-8') as file:
            json.dump(country_data, file, indent=4, ensure_ascii=False)
            break
    try:
        get_country = CountryInfo(country_name)
        data = get_country.info()
        # pprint(data, sort_dicts=False)

        name = data['name']
        area = data['area']
        capital = data['capital']
        population = data['population']
        currencies = data['currencies']
        languages = data['languages']
        region = data['region']

        print(f'''Siz {country_name} davlati haqidagi malumotlar:
{name} davlati {region} qit asida joylashgan bolib,
uning hududi {area} km.kv.
Poytaxti: {capital} shaxri.
Aholi soni: {population} insonni tashkil etadi.
Qabul qilingan tillar: {languages}.
Pil birliklari: {currencies}
''')
        country_data.append({
            'name': name,
            'area': area,
            'population': population,
            'capital': capital,
            'languages': languages,
            'currencies': currencies,
            'region': region
        })

    except Exception as e:
        print('Davlat nomi xato kiritildi!')

import requests

API = '6418b539e0697f54de8a3df65ebe9444'

parameters = {
    'appid': API,
    'units': 'metric',
    'lang': 'uz'
}


while True:
    city_name = input('Shaxar nomini kiriting !')

    try:
        parameters['q'] = city_name
        request = requests.get('https://api.openweathermap.org/data/2.5/weather?',
                                params=parameters)

        name = request['name']
        description = request['weather'][0]['description']
        temp = request['main']['temp']
        wind_speed = request['wind']['speed']

        print(f'''{name} shaxrida ob-havo {description}
Havo harorati: {temp} *
Shamol tezlig: {wind_speed} m/sek''')


    except:
        print('Davlat nomi xato kiritildi!')


