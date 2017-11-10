# /cat
# GET
# proper response:
#     200: data

import requests
resp = requests.get('http://py.net/cat')
with open('cat1.jpg', 'wb') as file:
    file.write(resp.content)