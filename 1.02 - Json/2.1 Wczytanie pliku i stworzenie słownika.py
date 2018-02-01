# 2.1	Wczytaj plik i stwórz słownik w którym kluczem będzie imię (i nazwisko) a wartością będzie słownik z kluczami kolor oczu i wzrost Przykład: {"Yoda": {"height": 66, "eyes": "brown"}}

file = open('py1.2.txt', 'r')
mydict={}
for data in file: #reads each line of file
    name=data[data.find(".") +2:data.find(" has")]  #searches for first " " and world " has", saves what's between
    eyes=data[data.find("has")+4:]
    eyes=eyes[:eyes.find(" and")]
    height=int(data[data.find(" is ")+3:data.find(" cm")])
    mydict[name]= {"Eyes: ": eyes, "Height: ": height}
print(mydict)
file.close()