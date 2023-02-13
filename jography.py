from codecs import open
import requests

def exchange():
    exc = data['rates']['RUB'] / data['rates'][l[3]]
    global round_exc
    round_exc = round(exc, 2)


url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
data = response.json()

while True:
    country = input("Введите страну: ")
    
    
    with open("africa.txt", "r", "utf_8_sig") as africa, open("america.txt", "r", "utf_8_sig") as america, \
    open("australia.txt", "r", "utf_8_sig") as australia, open("eurasia.txt", "r", "utf_8_sig") as eurasia:

        
        for line in africa:
            if country.title() in line:
                l = line.split(", ")
                exchange()
                if country.title() == l[0]:
                    print(f"Страна {country} находится в Африке. Столица: {l[1]}. Валюта: {l[2]}. Курс валюты к рублю РФ: {round_exc}")
        for line in america:
            if country.title() in line:
                l = line.split(", ")
                exchange()
                if country.title() == l[0]:
                    print(f"Страна {country} находится в Америке. Столица: {l[1]}. Валюта: {l[2]}. Курс валюты к рублю РФ: {round_exc}")
        for line in australia:
            if country.title() in line:
                l = line.split(", ")
                exchange()
                if country.title() == l[0]:
                    print(f"Страна {country} находится в Австралии. Столица: {l[1]}. Валюта: {l[2]}. Курс валюты к рублю РФ: {round_exc}")
        for line in eurasia:
            if country.title() in line:
                l = line.split(", ")
                exchange()
                if country.title() == l[0]:
                    print(f"Страна {country} находится в Евразии. Столица: {l[1]}. Валюта: {l[2]}. Курс валюты к рублю РФ: {round_exc}")