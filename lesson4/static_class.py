class MyClass(object):
    def __init__(self, data):
        self.data = data

    def create(self):
        print(self.data)

    @staticmethod
    def smethod(*arg):
        """
        :param arg: any data you'd like to enter
        """
        print 'Static:', arg

    @classmethod
    def cmethod(*arg):
        print 'Class:', arg

myclass = MyClass(23)
myclass.create()
myclass.smethod(23, 88, 89)
myclass.cmethod()
MyClass.smethod()
MyClass.cmethod()