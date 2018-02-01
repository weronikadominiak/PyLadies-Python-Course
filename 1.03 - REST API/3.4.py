# User status - get:
#
# /user_status
# GET
# proper response:
#     200: {string: string}
# User status - set:
#
# /user_status/set
# POST
# requires:
#     "api_key": string
#     "status": string
# proper response:
#     {'success': True}

import requests
resp1 = requests.post(
    'http://py.net/auth',
    json={
        "name": "WeronikaF",
        "password": "ziemniaki"
    }
)

resp2 = requests.post(
    'http://py.net/user_status/set',
    json={
        "api_key": resp1.json()["api_key"],
        "status": "Nieobecna"
    }
)
print(resp2.json())

resp3 = requests.get('http://py.net/user_status/')
print(resp3.json()['WeronikaF'])
print(resp3.json()['JAnholcer'])
