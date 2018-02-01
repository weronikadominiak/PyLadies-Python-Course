# Napisz program, który w zależności od opcji podanej przez użytkownika (1, 2 lub 3)
# odczyta odpowiednio plik x.txt, y.txt lub z.txt (zawartość dowolna)
# obsługa błędów powinna obejmować (co najmniej) komunikat o nieprawidłowej opcji,
# zaś wczytywanie treści pliku powinno znaleźć się w oddzielnej funkcji (wraz z obsługą błędów)
name = input("Choose file to read: 1/2/3? \n")

if name == "1":
    name = "z"
elif name == "2":
    name = "y"
elif name == "3":
    name = "x"

def read_file(name):
    file = open("files/" + name + ".txt" )
    data = file.read()
    print(data)

try:
    read_file(name)

except FileNotFoundError:
    print("You have to choose 1, 2 or 3!")