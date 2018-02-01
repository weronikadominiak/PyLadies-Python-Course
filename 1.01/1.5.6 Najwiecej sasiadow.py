from countries import countries
iloscgranic = 0
for i in countries:
    if len(i["borders"])>iloscgranic:
        iloscgranic = len(i["borders"])
        panstwo = i["name"]["common"]
print(panstwo, iloscgranic)
