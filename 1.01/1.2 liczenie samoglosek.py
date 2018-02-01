def policz_samogloski(zdanie):
    x=0
    zdanie=zdanie.lower()
    for letter in zdanie:
        samogloski= "aeiouyąę"
        if letter in samogloski:
            x+=1
    return x
print(policz_samogloski("Ala ma kota"))
print(policz_samogloski("Pies psu niedzwiedziem"))