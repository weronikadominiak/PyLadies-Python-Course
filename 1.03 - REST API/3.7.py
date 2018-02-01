import requests

# resp = requests.get("https://swapi.co/api/planets/1/")
# print(resp.json()["residents"])

resp = requests.get("https://swapi.co/api/people/")
print(resp.json()['results'])

for person in resp:
    if "https://swapi.co/api/planets/1/" in resp.json()[person]['results']['homeworld']:
        print(person)



