import json

def leerjson():
    with open('filejson.json') as file:
        data = json.load(file)
        print("ESTRUCTURA JSON", type(file))
    file.close()
    print(data)
    return data
def elementos():
    dict = leerjson()
    for element in dict:
            print(element)
