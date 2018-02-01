# /query_string
# GET
# proper response:
#     200: {
#     "parsed": bool,
#     "args": dict,
#     "url": dict,
#     "query_string": dict
# }

import requests
# resp = requests.get('http://py.net/query_string')
# print(resp.json())
resp = requests.get("http://py.net/query_string/?halo=1&weronika=ziemniak&costam=niewiemco")
print(resp.json())