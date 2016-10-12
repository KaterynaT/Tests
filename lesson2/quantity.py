"""
Output the list of "quantity", sorted by "ring_size".
Count down the total quantity of the items.
"""

import json


with open('ring.json') as f:
    sum = 0
    data = json.load(f)
    w = []
    o = []
    dct2 = {}
    dct = {}
    for i in data:
        t = i['inventory']['quantity']
        sum = sum + t
        y = int(i['inventory']['variant']['ring_size'])
        w.append(y)
        o.append(t)
    dct2 = dict(zip(w, o))

    for m in w:
        if m in dct:
            dct[m] = dct[m] + 1
        else:
            dct[m] = 1

    for i in sorted(dct):
        print(" Ring size %d : Quantity %d" % (i,dct[i]*dct2[i]))

    print "Toatal quantity of items:  ",sum

