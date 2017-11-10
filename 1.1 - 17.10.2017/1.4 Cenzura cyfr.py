def cenzura_cyfr(zdanie):
    cyfry="0123456789"
    nowezdanie=""
    for letter in zdanie:
        if letter in cyfry:
            letter ="#"
            nowezdanie += letter
        else:
            nowezdanie+=letter

    return nowezdanie

print(cenzura_cyfr("a1a ma k0ta"))
print(cenzura_cyfr("password12345"))
