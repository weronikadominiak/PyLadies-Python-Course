def podzielna(liczba, podzielna_przez):
    """
    Cos tam cos tam
    """
    return liczba % podzielna_przez == 0


def ugly(liczba):
    """
    Cos tam cos tam
    """
    if liczba == 1:
        return True
    for i in [2, 3, 5]:
        if podzielna(liczba, i):
            return True
    return False


print(ugly(11))
print(ugly(12))


def time(czas, jednostka):
    """
    Cos tam cos tam
    """
    hour, min, sec = czas.split(':')
    hour = int(hour)
    min = int(min)
    sec = int(sec)
    if jednostka == 'sec':
        return hour * 3600 + min * 60 + sec
    elif jednostka == 'min':
        return hour * 60 + min + round(sec / 60, 2)
    else:
        return hour + round(min / 60, 2) + round(sec / 3600, 2)


print(time('01:15:59', 's'))
print(time('01:15:59', 'm'))
print(time('01:15:59', 'h'))

result = []
r2 = []


def flatten(arr):
    """
    Cos tam cos tam
    """
    for el in arr:
        if isinstance(el, list):
            flatten(el)
        else:
            result.append(el)
    return result


def flattenNR(arr):
    """
    Cos tam cos tam
    """
    while True:
        el = arr.pop()
        if not isinstance(el, list):
            r2.append(el)
        else:
            arr = el
        if len(arr) == 0:
            break
    return r2[::-1]


print(flatten([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e']))
print(flattenNR([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e']))


def weird_power(a):
    """
    Cos tam cos tam
    """
    return a ** 2, a ** 3


def calculate(afun, data):
    """
    Cos tam cos tam
    """
    return afun(weird_power(data))



a = 3


def b(a):
    """
    Cos tam cos tam
    """
    sum(a)
    return a


b = b(a)
c = calculate(b, a)
print(c)


def d(a):
    """
    Cos tam cos tam
    """
    sorted(a)
    return a

d = d(a)
f = calculate(d, a)
print(f)


def power_2(a):
    """
    Cos tam cos tam
    """
    return (a + 0.5 * a) ** 2


print(power_2(3))


def a(a):
    """
    Cos tam cos tam
    """
    x = (a + 0.5 * a) ** 2
    return print(x(3))


data = [(9, 0), (1, 2), (3, 4)]
sorted_data = sorted(data, key=lambda a: a[0], reverse=False)
max_data = max(data, key=lambda a: max(a))
min_data = min(data, key=lambda a: max(a))
filtered_data = list(filter(lambda a: sum(a) > 5, data))

print({
    'a': {
        'a': {
            'a': {
                'a': {
                    'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {
                        'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {
                            'a': {'a': {'a': 1}}}}}}}}}}}}}}}}}}}}}}
})
