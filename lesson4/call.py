# -*- coding: utf-8 -*-


class A:
    @staticmethod
    def printint(*args):
        """
        :param args: any argument, that can be entered
        """
        print "Это integer"
    def printfloat(self):
        print "Это float"
    def printstr(self):
        print "Это string"

    def __call__(self, name):
        """
        :param name: any data(integer, float, string etc.)
        """
        try:
            getattr(self, "print%s" % type(name).__name__).__call__()
        except:
            print "Введенный тип данных не поддерживается"
            # return int

class B(A):
    def printlist(self):
        print "Это список"


A()(5)