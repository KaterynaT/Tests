"""
Write down the fibonacci function, using the "memorize" decorator for decreasing the algorithm complexity.
"""

from functools32 import wraps


def memorize(max_length=5):
    memo = {}

    def real_decorator(function):
        @wraps(function)
        def wrapper(args):
            if memo.get(args, None):
                return memo[args]
            else:
                remembered_fibonacci_number = function(args)
                memo[args] = remembered_fibonacci_number
                if len(memo) == max_length:
                    del(memo[memo.keys()[0]])
            # print remembered_fibonacci_number
            # print memo
            return remembered_fibonacci_number
        return wrapper
    return real_decorator


@memorize()
def fibonacci(n):
    # print('***')
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print (fibonacci(19))
print('=' * 10)
print (fibonacci(34))

