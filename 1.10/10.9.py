# Napisz aplikację, która będzie pozwalała założyć w niej konto posiadające login i hasło.
# Dane użytkowników trzymaj w słowniku. Pamiętaj żeby sprawdzić czy użytkownik o danym loginie już nie istnieje.
# Aplikacja też powinna pozwolić zalogować się wykorzystując login i hasło.

storage = {'weronika': 'haslo'}

login = input("Login: \n")

if login in storage:
    print("Username taken")
else:
    pass

password = input("Password: \n")


def createUser(log, passw):

    storage[log] = passw
    print("User created!")
    return storage

createUser(login, password)

def loginUser():
    login = input("Login: \n")
    password = input("Password: \n")
    if storage[login] == password:
        print("Succes!")
    else:
        print("Wrong password or login")
loginUser()
