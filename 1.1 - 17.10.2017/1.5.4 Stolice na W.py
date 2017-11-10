from countries import countries #żeby to zdadziałało, do folderu w którym znajduje się countries.py dodaje się plik __init__.py, żeby phyton wiedział że folder zawiera paczke
lista=[]
for i in countries: #dla każdego państwa z listy
    for letter in i["capital"]:
        if letter in "W":
            print(i["name"]["common"])
            print(i["capital"])

#druga opcja

for i in countries: #dla każdego państwa z listy
    if i["capital"].startswith("W"):
        print(i["name"]["common"])
        print(i["capital"])

