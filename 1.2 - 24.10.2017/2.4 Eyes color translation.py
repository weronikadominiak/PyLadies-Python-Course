file = open('py1.2.txt', 'r')
mydict={}
for data in file: #reads each line of file
    name=data[data.find(".") +2:data.find(" has")]  #searches for first " " and world " has", saves what's between
    eyes=data[data.find("has")+4:]
    eyes=eyes[:eyes.find(" and")]
    height=int(data[data.find(" is ")+3:data.find(" cm")])
    mydict[name]= {"Eyes: ": eyes, "Height: ": height}

file.close()

#nie sa rozdzielone dwukolorowe oczy!

eye_dict={}
for name in mydict:
    eyesc = mydict[name]["Eyes: "]
    height = mydict[name]["Height: "]
    if eyesc in eye_dict: #if color is allready in dic
        eye_dict[eyesc].append(height) #append value of height
    else: #if color is on in dict yet, create new key and it's first value equal height
        eye_dict[eyesc] = [height]

pl_eyesc = ""
for eyesc in eye_dict:
    avg = sum(eye_dict[eyesc])/len(eye_dict[eyesc])
    if "yellow" in eyesc: #translating eye color to Polish
        pl_eyesc = "zoltym"
    elif "black" in eyesc:
        pl_eyesc = "czarnym"
    elif "orange" in eyesc:
        pl_eyesc = "pomaranczowym"
    elif "blue" in eyesc:
        pl_eyesc = "niebieskim"
    elif "green" in eyesc:
        pl_eyesc = "zielonym"
    elif "red" in eyesc:
        pl_eyesc = "czerwonym"
    elif "brown" in eyesc:
        pl_eyesc = "brazowym"
    elif "gold" in eyesc:
        pl_eyesc = "zlotym"
    elif "blue-gray" in eyesc:
        pl_eyesc = "niebiesko-szarym"
    elif "pink" in eyesc:
        pl_eyesc = "rozowym"
    elif "hazel" in eyesc:
        pl_eyesc = "piwnym"
    else:
        pl_eyesc = "nieznanym"

    print("Sredni wzrost osob z kolorem oczu {} wynosi {}".format(eyesc, avg))