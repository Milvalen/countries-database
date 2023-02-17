from codecs import open
import pandas as pd
import requests

def exchange():
    exc = data['rates']['RUB'] / data['rates'][l[3]]
    global round_exc
    round_exc = round(exc, 2)
def population():
    for line in pop:
        p = line.split(",")
        if l[4] == p[2]:
            print(f"Население в стране {country}: {p[3]} человек") # функция, выдающая население страны


try:
    pd.read_html(requests.get('https://www.worldometers.info/world-population/population-by-country/').content)[-1].to_csv('pop.csv') 
    # таблица с населением


    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    data = response.json() # API с кодами валют и их курсом


    while True:
        country = input("Введите страну: ")
        
        
        with open("africa.txt", "r", "utf_8_sig") as africa, open("america.txt", "r", "utf_8_sig") as america, \
            open("australia.txt", "r", "utf_8_sig") as australia, open("eurasia.txt", "r", "utf_8_sig") as eurasia, \
            open("pop.csv", "r", "utf_8_sig") as pop: # цикл с файлами

            
            for line in africa:
                if country.title() in line:
                    l = line.split(", ")
                    exchange()
                    if country.title() == l[0]:
                        print(f"Страна {country} находится в Африке. Столица: {l[1]}. Валюта: {l[2]}. Курс валюты к рублю: {round_exc}")
                        population()
            for line in america:
                if country.title() in line:
                    l = line.split(", ")
                    exchange()
                    if country.title() == l[0]:
                        print(f"Страна {country} находится в Америке. Столица: {l[1]}. Валюта: {l[2]}. Курс валюты к рублю: {round_exc}.")
                        population()
            for line in australia:
                if country.title() in line:
                    l = line.split(", ")
                    exchange()
                    if country.title() == l[0]:
                        print(f"Страна {country} находится в Австралии. Столица: {l[1]}. Валюта: {l[2]}. Курс валюты к рублю: {round_exc}")
                        population()
            for line in eurasia:
                if country.title() in line:
                    l = line.split(", ")
                    exchange()
                    if country.title() == l[0]:
                        print(f"Страна {country} находится в Евразии. Столица: {l[1]}. Валюта: {l[2]}. Курс валюты к рублю: {round_exc}")
                        population() # основной цикл   
except: 
    print("Нет подключения к интернету")
    input()
