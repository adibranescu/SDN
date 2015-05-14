import requests
import json

baseURL = "https://sandboxapic.cisco.com/api/v0"

#Get network-device by IP
req = requests.get(baseURL + "/network-device/ip-address/40.0.1.6")
req_json = req.json()
print(json.dumps(req_json, indent = 4))

device_id = req_json["response"]["id"]

#IOS configuration
req2 = requests.get(baseURL + "/network-device/{}/config".format(device_id))
req2_json = req2.json()
print(req2_json["response"])

#interface information
req3 = requests.get(baseURL + "/interface/network-device/{}".format(device_id))
req3_json = req3.json()
print(json.dumps(req3_json, indent = 4))

#ACL information
req4 = requests.get(baseURL + "/acl/device/{}".format(device_id))
req4_json = req4.json()
print(json.dumps(req4_json, indent = 4))
