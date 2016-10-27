"""
Make "Mixin" for adding to your Class the function "Name_of_class", which would return the name of the current Class.
Create the function name_of_class in your class MyClass, that would print something and then call the parent's function
(make out what is "super"(in respect to inheritance) and use it in MyClass)
"""


class Mixin(object):
    def name_of_class(self):
        print "You've added mixin to %s" % self.__class__.__name__


class MyClass(Mixin):
    def name_of_class(self):
        print "This is my class"
        super(MyClass, self).name_of_class()

obj = MyClass()
obj.name_of_class()

