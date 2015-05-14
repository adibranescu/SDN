#IP: 172.16.14.158:3000

import requests
import json

baseURL = "http://172.16.14.158:3000"

for i in range(1000, 10000, 1):
    req = requests.delete(baseURL + "/masters/{}".format(i))
req_json = req.json()

print(json.dumps(req_json, indent=4))

req2 = requests.get(baseURL + "/masters")
req2_json = req2.json()
print(json.dumps(req2_json, indent=4))
