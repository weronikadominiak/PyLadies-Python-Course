from flask import Flask, request
import uuid
app = Flask(__name__)

users = {}

@app.route("/user/<username>/login", methods=["POST"])
def login(username):
    global users
    data = request.get_json()
    if users[username] == data["password"]:
        return "Login succesful! Your uuuid: " + str(uuid.uuid4())
    else:
        return "Wrong password!"