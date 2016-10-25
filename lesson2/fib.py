"""
Write down the fibonacci function, using the "memorize" decorator for decreasing the algorithm complexity.
"""

from functools32 import wraps


def memorize(max_length=5):
    memo = {}

    def real_decorator(function):
        @wraps(function)
        def wrapper(value):
            if memo.get(value):
                return memo[value]
            else:
                memo[value] = function(value)
                if len(memo) == max_length:
                    del(memo[memo.keys()[0]])
            return function(value)
        return wrapper
    return real_decorator


@memorize()
def fibonacci(n):
    # print('***')
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print (fibonacci(10))
# print('=' * 10)
# print (fibonacci(34))
