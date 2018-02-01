from math import gcd
def odwazniki(wagaA,wagaB):
    if wagaA == wagaB:
        return 1, 1
    elif wagaA != wagaB:
        nwd=gcd(wagaA, wagaB)
        liczbaodwaznikowA = wagaB/nwd
        liczbaodwaznikowB = wagaA/nwd
    return liczbaodwaznikowA, liczbaodwaznikowB
print(odwazniki(2,8))
print(odwazniki(4,6))
