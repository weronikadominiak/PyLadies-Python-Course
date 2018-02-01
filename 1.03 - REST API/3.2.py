# /register
# POST
# requires:
#     "name": string
#     "password": string
# proper response:
#     200: {'success': True}

import requests
resp = requests.post(
    'http://py.net/register',
    json={
        "name": "WeronikaF",
        "password": "ziemniaki"
    }
)
print(resp.json())