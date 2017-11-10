# 2.5 Znajdź i zapisz wszystkie imiona kobiet do pliku sw_women a wszystkich mężczyzn do sw_men

import json
with open('py1.2.json', 'r') as file:
    data = json.load(file)
    for person in data:
        if "female" in person["gender"]:
            sw_women = open('sw_women.txt', 'a')
            json.dump(person["name"], sw_women)
            sw_women.writelines("\n")
            sw_women.close()
        elif "male" in person["gender"]:
            sw_men = open('sw_men.txt', 'a')
            json.dump(person["name"], sw_men)
            sw_men.writelines("\n")
            sw_men.close()
