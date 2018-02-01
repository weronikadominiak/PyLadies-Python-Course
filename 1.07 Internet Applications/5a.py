# Napisz program, który pod adresem /users/add będzie przyjmował zapytania POST z JSON-em o następującej strukturze:
# {"imie": "Grzegorz", "wiek": "26", "plec": "m"}
# W wyniku takiego zapytania dane osoby należy zapisać na serwerze.

from flask import Flask, request

app = Flask(__name__)

users = {}

@app.route("/users/add", methods=["POST"])
def addUser():
    global users
    user = request.get_json()
    return str(user)

app.run(debug=True)