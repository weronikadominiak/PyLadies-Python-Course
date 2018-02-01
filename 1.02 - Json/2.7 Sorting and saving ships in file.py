# 2.7 Wczytaj zawarty w pliku json. Stwórz plik który będzie posiadał wszystkie statki w zdaniach od najdroższego do najtańszego: <Nazwa> kosztuje <123> credits.

import json
with open('py1.2zd.json', 'r') as file:
    data = json.load(file)
    all_ships = open('all_ships.txt', 'a')
    for ship in data:
        json.dump(ship["name"] + " kosztuje " + ship["cost_in_credits"] + " credits.", all_ships)
        all_ships.writelines("\n")

#trzeba posortowac jeszcze!
