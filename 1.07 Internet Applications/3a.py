from flask import Flask, request

app = Flask(__name__)

users = {}

@app.route("/user/<username>/set-password", methods=["POST"])
def setPassword(username):
    global users
    data = request.get_json()
    new_password =data["password"]
    users[username] = new_password
    return "set password of {} to {}".format(username, new_password)

@app.route("/users", methods=["GET"])
def showUsers():
    return str(users)

app.run(debug=True)