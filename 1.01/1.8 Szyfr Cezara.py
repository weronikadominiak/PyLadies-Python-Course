def cezar(tekst, przesuniecie):
    nowytekst = ""
    for letter in tekst:
        numer=ord(letter) # w numer zapisuje numerek literki
        numer += przesuniecie # uwzględnia i zapisuje przesunięcie
        if letter.isalpha(): # jeśli letter jest literą
            if letter.islower(): #jeśli litera jest małą literą
                if numer > ord("z"):
                    numer -= 26
                elif numer < ord("a"):
                    numer += 26
            else: # else, czyli jeśli jest wielką literą, można też użyć nowego ifa z letter.isupper
                if numer > ord("Z"):
                    numer -= 26
                elif numer < ord("A"):
                    numer += 26
            nowytekst += chr(numer)
        elif letter.isalnum(): # jeśli "litera" jest cyfrą, dodaj cyfrę do nowego stringa
            nowytekst += letter
        elif letter in " ": # uwzględnienie spacji
            nowytekst += " "
    return nowytekst
print(cezar("abc ABC", -2))
