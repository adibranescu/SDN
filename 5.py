import json # Parse JSON data

masters = {}
masters["Yoda"] = "Green"
masters["Mace Windu"] = "Purple"
masters["Obi-Wan Kenobi"] = ["Blue", "Green"]

print(masters)

for master, lightsaber in masters.items():
    print("{} uses a {} lightsaber".format(master, lightsaber))

del masters["Mace Windu"]

print(json.dumps(masters, indent=4))
