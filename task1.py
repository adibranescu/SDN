import requests
import json

baseURL = "https://sandboxapic.cisco.com/api/v0"

#Get all network devices info

req = requests.get(baseURL + "/network-device")

req_json = req.json()

print(json.dumps(req_json, indent = 4))


#Retrieve all the hosts in the network

req = requests.get(baseURL + "/host")

req_json = req.json()

print(json.dumps(req_json, indent = 4))
