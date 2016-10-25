"""
Make "Mixin" for adding to your Class the function "Name_of_class",
which would return the name of the current Class
"""


class BaseClass:
    def Name_of_class(self):
        print "Base Class"

class Mixin(object):
    def name_of_class(self):
        print "You've added mixin to %s" % self.__class__.__name__

class MyClass(Mixin):
    pass

obj = MyClass()
obj.name_of_class()

