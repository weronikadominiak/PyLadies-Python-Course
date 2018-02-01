from flask import Flask, request

app = Flask(__name__)

status ="Data"
@app.route("/current-status", methods=["POST", "GET"])
def setStatus():
    global status
    if request.method == "GET":
        return status
    else:
        data = request.get_json()
        status = data["status"]
        return "Saved status: {}".format(status)

app.run(debug=True)