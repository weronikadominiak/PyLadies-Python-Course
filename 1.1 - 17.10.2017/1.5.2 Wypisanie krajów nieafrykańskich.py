from countries import countries #żeby to zdadziałało, do folderu w którym znajduje się countries.py dodaje się plik __init__.py, żeby phyton wiedział że folder zawiera paczke
lista=[]
for i in countries: #dla każdego państwa z listy
    if i["region"]!="Africa":
        lista.append(i["name"]["common"]) #lub print(i["name"]["common"])
print(lista)
