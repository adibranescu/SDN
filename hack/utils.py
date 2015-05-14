import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module

requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3

apicem_ip = "sandboxapic.cisco.com"
baseUrl = "https://"+apicem_ip+"/api/v0"


def get_location():

    resp = requests.get(baseUrl + "/location", verify=False)
    response_json = resp.json()
#   print ("Status: ", resp.status_code)
    return response_json["response"]


def post_location(form):

    r_json = {
    "description": "Demo Create Loaction",
    "locationName": "Building123",
    "civicAddress": "123 Lucky Drive MILPITAS, CALIFORNIA 95035",
    "geographicalAddress": "Latitude: 37.422039, Longitude: -121.81659 degrees"
    }   

    headers = {'content-type': 'application/json'}
    r = requests.post(baseUrl + '/location', json.dumps(r_json), headers=headers, verify=False)
    print("Status: ", r.status_code)
    print(r.text)
    
    if r.status_code == 202 or r.status_code == 200:
        task_url = r.json()["response"]["url"]
        print('https://' + apicem_ip + task_url)
        task = requests.get('https://' + apicem_ip + task_url, verify=False)
        task_json = task.json()
        return task_json.get("isError", None)
    else:
        return None


def get_network_device():

    device_list = []
    count = requests.get(baseUrl + '/network-device/count', verify=False).json()["response"]
    resp = requests.get(baseUrl + '/network-device/1/{}'.format(count), verify=False)
    response_json = resp.json()
    for item in response_json["response"]:
        device_list.append({
            "id": item["id"],
            "hostname": item["hostname"],
            "managementIpAddress": item["managementIpAddress"],
            "macAddress": item["macAddress"],
            "type": item["type"],
            "vendor": item["vendor"],
            "upTime": item["upTime"]
        })
    return device_list


def post_network_device_location(device_id, location_id):

    r_json = {
    "id": device_id,
    "location": location_id
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(baseUrl + '/network-device/location', json.dumps(r_json), headers=headers, verify=False)
    print("Status: ", r.status_code)
    print(r.text)
    return r.status_code


def get_network_device_location(id):
    ret = requests.get(baseUrl + '/network-device/{}/location'.format(id), verify=False)
    return ret.json()["response"]["location"]


def get_location_by_id(id):
    ret = requests.get(baseUrl + '/location/{}'.format(id), verify=False)
    return ret.json()["response"]


# if post_location(None) == None:
#     print("Location added")
# else:
#     None

# print("Locations:\n" + json.dumps(get_location(), indent=4))
# print("Network devices:\n" + json.dumps(get_network_device(), indent=4))
# #post_network_device_location("a632c6e8-89bf-4949-8e4d-a249105f2c7c", "255f8f86-554f-473f-aa35-ee238ad11c0a")
# print("Location of the device with id: a632c6e8-89bf-4949-8e4d-a249105f2c7c:")
# location_id = get_network_device_location("a632c6e8-89bf-4949-8e4d-a249105f2c7c")
# print(json.dumps(get_location_by_id(location_id), indent=4))


test_json = {
  "response": [
    {
      "id": "ed4c5927-118c-485c-97b3-00390d42c7f1",
      "civicAddress": "tefdgfds",
      "geographicalAddress": "Latitude: 2312.312312, Longitude: 31.321312                 degrees",
      "description": "test",
      "locationName": "Test"
    },
    {
      "id": "7c1cd09f-f29f-4045-9c46-f14e11899180",
      "civicAddress": "fsdafds",
      "geographicalAddress": "Latitude: fdsafds, Longitude: fdsafds                 degrees",
      "description": "fdsafds",
      "locationName": "dsadas"
    }
  ],
  "version": "0.0"
}


def coord_list(location_json):
#   location_json = get_location()
    c_list = []
    for item in location_json["response"]:
        [lat, lon] = item["geographicalAddress"].split(",")
        lat_value = lat.split(" ")[1]
        lon_value = lon.split(" ")[2]
        c_list.append((lat_value, lon_value))
    return c_list

print(json.dumps(test_json, indent=4))
print(coord_list(test_json))
    
def map_device_location():
    list_mapping = []
    ret = requests.get(baseUrl + '/network-device/location', verify=False)
    for item in ret.json()["response"]:
        device = requests.get(baseUrl + '/network-device/{}'.format(item["id"]), verify=False)
        location = requests.get(baseUrl + '/location/{}'.format(item["location"]), verify=False)
        list_mapping.append((device.json()["response"], location.json()["response"]))
    return list_mapping
