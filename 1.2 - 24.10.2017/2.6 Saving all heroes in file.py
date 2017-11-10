# 2.6 Zapisz plik sw_all_heros z bohaterami w zdaniach: <Imie> wazy <waga> kg jest <plec> i pochodzi z <Planeta>. Przykład: Anakin Skywakaer waży 90 kg jest mężczyzną i pochodzi z Tatuin.

import json
with open('py1.2.json', 'r') as file:
    data = json.load(file)
    sw_all_heroes = open("sw_all_heroes.txt", "a")
    for hero in data:
        if "female" in hero["gender"]:
            gender = "kobieta"
        elif "male" in hero["gender"]:
            gender = "mezczyzna"
        else:
            gender = "nienznanej plci"
        json.dump(hero["name"] + " wazy " + hero["mass"] + " kg, jest " + gender + " i pochodzi z "+ hero["homeworld"] +".", sw_all_heroes)
        sw_all_heroes.writelines("\n")