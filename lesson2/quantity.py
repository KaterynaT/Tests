"""
Output the list of "quantity", sorted by "ring_size".
Count down the total quantity of the items.
"""

import json


def products(any_json_file):
    total_quantity = 0
    items = {}
    with open(any_json_file) as f:
        data = json.load(f)
        for i in data:
            quantity = i['inventory'].get('quantity')
            total_quantity = total_quantity+quantity
            ring_size = int(i["inventory"]['variant'].get('ring_size'))
            if ring_size in items:
                items[ring_size] += quantity
            else:
                items[ring_size] = quantity
        for i in sorted(items):
            print(" Ring size %d - Quantity %d" % (i, items[i]))
        print "Total quantity of items:",total_quantity

    return total_quantity


if __name__ == "__main__":
    products('ring.json')



# with open('ring.json') as f:
#     sum = 0
#     data = json.load(f)
#     w = []
#     o = []
#     dct2 = {}
#     dct = {}
#     for i in data:
#         t = i['inventory']['quantity']
#         sum = sum + t
#         y = int(i['inventory']['variant']['ring_size'])
#         w.append(y)
#         o.append(t)
#     dct2 = dict(zip(w, o))
#
#     for m in w:
#         if m in dct:
#             dct[m] = dct[m] + 1
#         else:
#             dct[m] = 1
#     for i in sorted(dct):
#         print(" Ring size %d : Quantity %d" % (i,dct[i]*dct2[i]))
#
#     print "Toatal quantity of items:  ",sum

