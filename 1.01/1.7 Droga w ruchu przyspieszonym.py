def droga (t,a,V0=0):
    s = V0*t + (a*(t**2))/2
    return s
print(droga(5,5))
print(droga(10,10, 100))