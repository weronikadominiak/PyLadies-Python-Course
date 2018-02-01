def policz_slowa(zdanie):
    lista =[]
    for word in zdanie:
        if " " in zdanie:
            y = zdanie.index(" ") #określam, gdzie jest white space i to co przed nim dodaje do listy, a kasuje ze stringa
            lista += [zdanie[:y]]
            zdanie = zdanie[y + 1:]
        elif " " not in zdanie:
            lista += [zdanie]  # zawsze zostaje jeden wyraz, ostatni, nie ma przed nim spacji, więc po prostu go dodaje osobno
            break
    x=len(lista)
    return x
print(policz_slowa("Ala ma kota"))
print(policz_slowa("Pies psu niedzwiedziem, bo tak"))


# mozna zrobic to w ten sposob to liczba spacji+1 to liczba slow
