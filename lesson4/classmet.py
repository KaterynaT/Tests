class BaseClass:
    def Name_of_class(self):
        print "Just the Base Class"


class Mixin(object):
    def name_of_class(self):
        print "You've added mixin to %s" % self.__class__.__name__

class MyClass(Mixin):
    pass

class ClassMet(object):
    @classmethod
    def name_of_class(self):
        print "And now you've added mixin to %s" % self.__class__.__name__

class AnotherClass(ClassMet):
    pass


obj = MyClass()
obj.name_of_class()
obj2 = AnotherClass()
obj2.name_of_class()
BaseClass().Name_of_class()