from codecs import open
import pandas as pd
import requests


pd.read_html(requests.get('https://www.worldometers.info/world-population/population-by-country/').content)[-1].to_csv('pop.csv') 
url = 'https://api.exchangerate.host/latest' # API с кодами валют и их курсом
response = requests.get(url)
data = response.json() 


while True: 
    country = input("Введите страну: ")

    
    # работа с файлами
    with open("countries.txt", "r", "utf_8_sig") as country_file, open("pop.csv", "r", "utf_8_sig") as pop:


        # работа с данными в базе
        for line in country_file:
            if country.title() in line:
                l = line.split(", ")
                exc = data['rates']['RUB'] / data['rates'][l[3]]
                round_exc = round(exc, 2)
                if country.title() == l[0]:
                    print(f"\nСтрана {country} находится в {l[5]}. Столица: {l[1]}. Валюта: {l[2]}. Курс валюты к рублю: {round_exc}")
                    
                    # статистика по населению
                    for line in pop:
                        p = line.split(",")
                        if l[4] == p[2]:
                            print(f"Население в стране {country}: {p[3]} человек\n")