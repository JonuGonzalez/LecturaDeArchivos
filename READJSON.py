import json

def leerjson():
    file = leerjson("filejson.json",)
    data = json.load(file)
    file.close()
    print(data)
    return data

dict = leerjson()
for element in dict:
    print(element)

