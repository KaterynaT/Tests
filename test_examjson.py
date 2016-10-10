import json


a_dict = {'Home_address': ' '}

with open ('examplejs.json') as f:
    data = json.load(f)
    for e in f:
        if e == "Home_address":
            print ("there is")
        else:
            print ("no information")


data.update(a_dict)

with open ('examplejs.json', 'w') as f:
    json.dump(data, f, indent=2)





