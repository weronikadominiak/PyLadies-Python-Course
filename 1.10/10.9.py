# Napisz aplikację, która będzie pozwalała założyć w niej konto posiadające login i hasło.
# Dane użytkowników trzymaj w słowniku. Pamiętaj żeby sprawdzić czy użytkownik o danym loginie już nie istnieje.
# Aplikacja też powinna pozwolić zalogować się wykorzystując login i hasło.

storage = {'weronika': 'haslo'}

#Login in if login isn't already taken:
while True:
    login = input("Login: \n")
    if login in storage:
        print("Username taken")
    else:
        break

password = input("Password: \n")

#check if password is correct
def createUser(log, passw):
    storage[log] = passw
    print("User created!")
    return storage

createUser(login, password)

#Repeat login until password and login are correct
def loginUser():
    while True:
        login = input("Login: \n")
        password = input("Password: \n")
        if storage[login] == password:
            print("Succes!")
            break
        else:
            print("Wrong password or login")

loginUser()
