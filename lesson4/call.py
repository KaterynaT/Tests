# -*- coding: utf-8 -*-
#
# class Name(object):
#     def __call__(self, a):
#         if type(a) == int:
#             print "Это integer"
#         elif type(a) == str:
#             print "Это string"
#         elif type(a) == float:
#             print "Это float"
#         print a
#         return a
#
#
# f = Name()
# f(9.9)


class A:
    def printint(self):
        print "Это integer"
    def printfloat(self):
        print "Это float"
    def printstr(self):
        print "Это string"

    def __call__(self, name):
        # print name
        # print ("print%s" % type(name).__name__)
        try:
            getattr(self, "print%s" % type(name).__name__).__call__()
        except:
            print "Введенный тип данных не поддерживается"
            return int

class B(A):
    def printlist(self):
        print "Это список"


obj = B()
obj(9.6)