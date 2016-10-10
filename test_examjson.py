import json


a_dict = {'Home_address': ' '}

with open('examplejs.json') as f:
    data = json.load(f)
    if 'Home_address' in data:
        print ('there is')
    else:
        data.update(a_dict)

with open('examplejs.json', 'w') as f:
    json.dump(data, f, indent=2)





