# 2.2 Zapisz wszystkie osoby wyższe niż 200 cm do pliku hero_200_plus a resztę do pliku hero_short.
file = open('py1.2.txt', 'r')
mydict={}
for data in file: #reads each line of file
    name=data[data.find(".") +2:data.find(" has")]  #searches for first " " and world " has", saves what's between
    height=int(data[data.find(" is ")+3:data.find(" cm")])
    mydict[name]= {}
    mydict[name]["Name: "]=name
    mydict[name]["Heigh: "]=height
    if height > 200:
        hero_200_plus = open('hero_200_plus.txt', 'a')
        hero_200_plus.writelines(name + ": " + str(height) + " cm")
        hero_200_plus.writelines('\n')
        hero_200_plus.close()
    else:
        hero_short = open('hero_short.txt', 'a')
        hero_short.writelines(name + ": " + str(height) + " cm")
        hero_short.writelines('\n')
        hero_short.close()

file.close()


