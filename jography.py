from codecs import open


while True:
    country = input("Введите страну: ")
    with open("africa.txt", "r", "utf_8_sig") as africa, open("america.txt", "r", "utf_8_sig") as america, \
    open("australia.txt", "r", "utf_8_sig") as australia, open("eurasia.txt", "r", "utf_8_sig") as eurasia:

        
        for line in africa:
            if country.title() in line:
                l = line.split(", ")
                if country.title() == l[0]:
                    print(f"Страна {country} находится в Африке. Столица: {l[1]}. Валюта: {l[2]}")
        for line in america:
            if country.title() in line:
                l = line.split(", ")
                if country.title() == l[0]:
                    print(f"Страна {country} находится в Америке. Столица: {l[1]}. Валюта: {l[2]}")
        for line in australia:
            if country.title() in line:
                l = line.split(", ")
                if country.title() == l[0]:
                    print(f"Страна {country} находится в Австралии. Столица: {l[1]}")
        for line in eurasia:
            if country.title() in line:
                l = line.split(", ")
                if country.title() == l[0]:
                    print(f"Страна {country} находится в Евразии. Столица: {l[1]}. Валюта: {l[2]}")
    africa.close()
    america.close()
    australia.close()
    eurasia.close()
    