# Napisz aplikację, która w zależności od argumentu "file" (GET) odczyta plik "hehe.txt",
# "heheszki.json" lub "beczka_smiechu.txt" (zawartość dowolna, powinny znajdować się w katalogu z aplikacją).
# Obsłuż sytuację, w której plik nie będzie istniał.


from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route("/<file>", methods=["GET", "POST"])
def read_file(file):
    try:
        file = open(file)
    except FileNotFoundError:
        return "Sorry file doesn"
        t
        exist!"

    data = file.read()
    return data


app.run(debug=True)