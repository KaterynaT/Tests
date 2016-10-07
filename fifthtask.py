# -*- coding: utf-8 -*-
import re
with open('350.txt') as file:
    a = file.read()
    a.decode('utf-8')
    g = re.findall(r'<b>(.*?)</b>', a, re.DOTALL)
    t = re.findall(r'</b>(.*?)</td>', a, re.DOTALL)
    p = re.findall(r'<td>(.*?)</td>', a, re.DOTALL)

    with open('350_1.txt', 'w') as f:
        f.write(' '.join(g))
        f.write(' '.join(t))
        f.write(' '.join(p))





