import json

def readJson(file):
    with open(file) as json_data:
        d = json.load(json_data)
        return d
