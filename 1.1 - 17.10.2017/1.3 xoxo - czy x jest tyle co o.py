def xo_checker(wyraz):
    x = 0
    o = 0
    for letter in wyraz:
        if letter in "x":
            x+=1
        elif letter in "o":
            o+=1
        else:
            return "Illegal letters in text"
    if x == o:
        wartosc="True"
    else:
        wartosc="False"
    return wartosc

print(xo_checker("xoxoxoxoxoxo"))
print(xo_checker("xxxoooxxxxxxxo"))
print(xo_checker("xpd"))
