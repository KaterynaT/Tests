def get_arguments(a, *args, **kwargs):
    """
    :param a: just the first argument
    :param args: any arguments,which will be raised to the third degree
    :param kwargs: key, value arguments
    """
    print "The first argument is ", a
    for arg in args:
        try:
            third_degree = int(arg) ** 3
            print "This argument is raised to the third degree:", third_degree
        except:
            print arg, "is not an integer and unfortunately cannot be raised to the third degree"

    for i, j in kwargs.items():
        if j == ": football":
            print "This is the best choice"
        print i, j

get_arguments(3,6,8, "poppopopot",9, name=': Bob', sport=': football', age=19)