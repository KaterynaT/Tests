from functools32 import wraps


def memorize(max_length=5):
    memo = {}

    def real_decorator(function):
        @wraps(function)
        def wrapper(args):
            # print(max_length, len(memo))
            if memo.get(args, None):
                return memo[args]
            else:
                rv = function(args)
                memo[args] = rv
                if len(memo) == max_length:
                    del(memo[memo.keys()[0]])
            return rv
        return wrapper
    return real_decorator


@memorize()
def fibonacci(n):
    print('***')
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print (fibonacci(19))
print('=' * 10)
print (fibonacci(40))
