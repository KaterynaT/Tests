# -*- coding: utf-8 -*-

class MyClass(object):
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        """
        :param value: any data for checking
        """
        self._x = value
        
    def del_x(self):
        self._x = 'No more'

    x = property(get_x, set_x, del_x)


print type(MyClass.x)
myclass = MyClass()
print MyClass().x
myclass.x = 90
print myclass.x
del myclass.x
print myclass.x



