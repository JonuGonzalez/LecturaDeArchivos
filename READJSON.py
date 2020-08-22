import json

def readjson():
    file = readjson("Archivos/filejson.json","r","error")
    data = json.load(file)
    file.close()
    print(data)
    return data

dict = readjson()
for element in dict:
    print(element)

