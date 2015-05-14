import requests
import json

baseURL = "https://sandboxapic.cisco.com/api/v0"

#Get all policies
req = requests.get(baseURL + "/policy")

req_json = req.json()

print(json.dumps(req_json, indent = 4))

#Get all applications
req = requests.get(baseURL + "/application")

req_json = req.json()

print(json.dumps(req_json, indent = 4))
