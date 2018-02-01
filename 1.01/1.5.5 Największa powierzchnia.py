from countries import countries
najwiekszapow= 0
for i in countries:
    if i["area"]>najwiekszapow:
        najwiekszapow = i["area"]
        panstwo=i["name"]["common"]
print(panstwo, najwiekszapow)
