from flask import Flask

app = Flask(__name__)

suma = ""

@app.route("/add/<liczba1>/<liczba2>")
def add(liczba1, liczba2):
    suma = int(liczba1) + int(liczba2)
    return "Suma wynosi {}".format(str(suma)) #return musi byc stringiem

app.run(debug=True)