"""
Count down and output the total quantity of "ones" in "ring.json" file.
"""

import json


def products(any_json_file):
    ones = 0
    with open(any_json_file) as f:
        data = json.load(f)
        data = str(data)
        for i in data:
            if i == '1':
                ones = ones+1
        print ones

if __name__ == "__main__":
    products('ring.json')

