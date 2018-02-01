# Napisz algorytm, który na wejście przyjmie listę zawierającą tylko stringi i integery.
# Zwróci listą zawierającą tylko powtarzające się wartości, nie zmieniając ich kolejności.
# Przykład: [1, 2, 3, 1, 3] 1 i 3 nie są unikalne, więc wynikiem będzie [1, 3, 1, 3].

my_list = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6, "a", "a"]

def non_unique_list(my_list):
    new_list = []
    for element in my_list:
        if my_list.count(element) > 1:
            new_list.append(element)

    return print(new_list)

non_unique_list(my_list)