# Napisz aplikację - na podstawie podanego szablonu - która po podaniu tekstu i liczby zwróci tekst "przesunięty w prawo"
# (uwaga: ograniczamy się do małych liter alfabetu łacińskiego) o liczbę podaną przez użytkownika (np. abcd -> bcde, zdcb -> aedc)
# Przydatne funkcje: chr, ord
# Przydatny operator: % (modulo)
# Przydatna informacja: alfabet łaciński ma 26 liter
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def cezar_handler():
    new_text = ""
    if request.method == "POST":
        user_text = request.form.get("text")
        user_offset = request.form.get("offset")

        def cezar(word, offset):
            new_text = ""
            offset = int(offset)
            for letter in word:
                numer = ord(letter)  # w numer zapisuje numerek literki
                numer += offset  # uwzględnia i zapisuje przesunięcie
                if letter.isalpha():  # jeśli letter jest literą
                    if letter.islower():  # jeśli litera jest małą literą
                        if numer > ord("z"):
                            numer -= 26
                        elif numer < ord("a"):
                            numer += 26
                    else:  # else, czyli jeśli jest wielką literą, można też użyć nowego ifa z letter.isupper
                        if numer > ord("Z"):
                            numer -= 26
                        elif numer < ord("A"):
                            numer += 26
                    new_text += chr(numer)
                elif letter.isalnum():  # jeśli "litera" jest cyfrą, dodaj cyfrę do nowego stringa
                    new_text += letter
                elif letter in " ":  # uwzględnienie spacji
                    new_text += " "

            return new_text
        new_text = cezar(user_text, user_offset)
        return render_template("cezar.html",
                               encrypted_text = new_text)

    return render_template("cezar.html")

app.run(debug=True)