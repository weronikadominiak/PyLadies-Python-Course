import json
import requests
from flask import Flask

app = Flask(__name__)


@app.route("/planet-details/<planet>", methods=["GET", "POST"])
def planet_details(planet):

    data = requests.get(
        "https://swapi.co/api/planets/?search=" + planet)
    planets = data.json()["results"]

    planet_data = planets[0]
    print(planet_data)
    response = "Na planecie {} panuje klimat {}, a liczba mieszkancow wynosi {}"\
        .format(planet, planet_data["climate"], planet_data["population"])

    return response


app.run(debug=True)