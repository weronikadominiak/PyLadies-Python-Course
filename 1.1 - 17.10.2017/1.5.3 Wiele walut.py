from countries import countries #żeby to zdadziałało, do folderu w którym znajduje się countries.py dodaje się plik __init__.py, żeby phyton wiedział że folder zawiera paczke

for i in countries: #dla każdego państwa z listy
    if len(i["currency"])>1:
        print(i["name"]["common"])
        print(i["currency"])


#druga opcja, z zapisaniem danych w słowniku zawartym w liscie
lista=[]
slownik={}
for i in countries: #dla każdego państwa z listy
    if len(i["currency"])>1:
        slownik["Name"]=i["name"]["common"]
        slownik["Currency"]=i["currency"]
        lista.append(dict(slownik))
print(lista)

