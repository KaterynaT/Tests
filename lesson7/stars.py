# -*- coding: utf-8 -*-
def stars(some_text = "TEST MODE - no records"):
    a = "*"*40
    b = "*"*2
    c = " "*36
    d = b+" "*7+some_text+ " "*7+b
    S = a+"\n"+b+c+b+"\n"+d+"\n"+b+c+b+"\n"+a
    print(S)

stars()
