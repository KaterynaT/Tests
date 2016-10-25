# def f(a,b=1)
# def f(a,b=1, c=3)
# def f(a,*some_array)
# def f(a, **some_dict)
# def f(a, some_array , *some_dict)
# def f(a, some_array, *some_dict, s, r=666)


def f(*args):
    return args

print f (5,3,1,3,7,9,9,9)

#
# def func(**kwargs, a = 1):
#     return kwargs
#
# print func(a, b=2, c=3)

#
def my_func(**kwargs):
    for i, j in kwargs.items():
        if j == ": football":
            print "This is the best choice"
        print i, j
my_func(name=': Bob', sport=': football', age=19)


def sum(*args):
    s = 0
    for i in args:
        s += i
    print "sum is", s

sum(4,6,78)

# def my_three(a, b, c):
#     print a, b, c
#
#
# a = [1, 2, 3]
# my_three(*a)


def get_arguments(a, *args):
    print "The first argument is ", a
    for arg in args:
        try:
            third_degree = int(arg) ** 3
            print "This argument is raised to the third degree:", third_degree
        except:
            print arg, "is not an integer and unfortunately cannot be raised to the third degree"
get_arguments(3,6,"poppopopot",9)


