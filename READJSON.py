import json

def readjson():
    file = open("filejson.json")
    data = json.load(file)
    file.close()
    print(data)
    return data

dict = readjson()
for element in dict:
    print(element)

