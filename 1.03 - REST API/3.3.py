# /auth
# POST
# requires:
#     "name": string
#     "password": string
# proper response:
#     {'api_key': string, 'name': string}

import requests
resp = requests.post(
    'http://py.net/auth',
    json={
        "name": "WeronikaF",
        "password": "ziemniaki"
    }
)
print(resp.json())