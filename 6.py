#IP: 172.16.14.158:3000

import requests
import json

baseURL = "http://172.16.14.158:3000"

req = requests.get(baseURL + "/masters", params={"lightsaber":"Green"})
req_json = req.json()

print(json.dumps(req_json, indent=4))
