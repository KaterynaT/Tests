
import requests
import json


def find_names(link = "https://api.github.com/repositories"):
    file = requests.get(link)
    content = json.loads(file.content)
    for i in content:
        name = i.get('name')
        print name
find_names()

