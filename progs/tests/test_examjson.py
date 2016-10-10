import sys
import json
sys.path.append('../')
import unittest


class TestJsonFile(unittest.TestCase):
    def testcheck(self):
        a_dict = {'Home_address': ' '}
        with open('examplejs.json') as f:
            data = json.load(f)
            if 'Home_address' in data:
                print ('there is')
            else:
                data.update(a_dict)

        with open('examplejs.json', 'w') as f:
            json.dump(data, f, indent=2)

    def testcheck2(self):
        a_dict = {'Ano_addr': ' '}
        with open('examplejs.json') as f:
            data = json.load(f)
            if 'Ano_addr' in data:
                print ('there is')
            else:
                data.update(a_dict)

        with open('examplejs.json', 'w') as f:
            json.dump(data, f, indent=2)









