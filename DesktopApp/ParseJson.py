import json

def saveJsonFile(data, filename):
    data = """{ "NetworkDevices" : """ + response.text + "}"
        data = json.loads(data)
        print(type(data))
        with open('Data.json', 'r') as file:
            json.dump(data, file, indent = 3)
            # data = json.load(file)
        print(data)