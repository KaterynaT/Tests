# -*- coding: utf-8 -*-

class Mixin(object):
    @classmethod
    def name_of_class(self):
        print "You've added mixin to %s" % self.__class__.__name__

class MyClass(Mixin):
    def name_of_class(self):
        print "This is my class"
        super(MyClass,self).name_of_class()

Mixin.name_of_class()
obj = MyClass()
obj.name_of_class()

#
# # Родительский класс
#
# class A(object):
#     def __init__(self):
#         print(u'конструктор класса A')
#
# # Потомок класса А
# class B(A):
#     def __init__(self):
#         print(u'конструктор класса B')
#         super(B, self).__init__()