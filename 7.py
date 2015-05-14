#IP: 172.16.14.158:3000

import requests
import json

baseURL = "http://172.16.14.158:3000"

req = requests.post(baseURL + "/masters", data={"name": "Ana", "lightsaber":"Black & Yellow"})
req_json = req.json()

print(json.dumps(req_json, indent=4))

req2 = requests.get(baseURL + "/masters")
req2_json = req2.json()
print(json.dumps(req2_json, indent=4))
