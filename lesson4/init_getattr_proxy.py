# -*- coding: utf-8 -*-


class Spare_parts:
    def transmission(self):
        print("Sparking plug is temporarily out of stock")

class Proxy:
    def __init__(self):
        self.__execution = Spare_parts()
    def __getattr__(self, name):
        """
        :param name: any name of method that you'd like to call
        """
        print ("Вызван метод %s" % name)
        try:
            return getattr(self.__execution, name)
        except:
            print "Нет такого метода"
            return int

obj = Proxy()
obj.transmission()
