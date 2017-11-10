file = open('py1.2.txt', 'r')
mydict={}
for data in file: #reads each line of file
    name=data[data.find(".") +2:data.find(" has")]  #searches for first " " and world " has", saves what's between
    eyes=data[data.find("has")+4:]
    eyes=eyes[:eyes.find(" and")]
    height=int(data[data.find(" is ")+3:data.find(" cm")])
    mydict[name]= {"Eyes: ": eyes, "Height: ": height}

file.close()

eye_dict={}
for name in mydict:
    eyesc = mydict[name]["Eyes: "]
    height = mydict[name]["Height: "]
    if eyesc in eye_dict:
        eye_dict[eyesc].append(height)
    else:
        eye_dict[eyesc] = [height]

for eyesc in eye_dict:
    avg = sum(eye_dict[eyesc])/len(eye_dict[eyesc])
    print("Sredni wzrost osob z kolorem oczu {} wynosi {}".format(eyesc, avg))

#co z dwukolorowymi oczami?