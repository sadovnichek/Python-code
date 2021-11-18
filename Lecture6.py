import timeit

def filter(func, iterable):
    for e in iterable:
        if func(e):
            yield e

def is_even(num):
    return num % 2 == 0

def map(func, *iterables):
    iters = [iter(iterable) for iterable in iterables]
    while True:
        try:
            args = [next(it) for it in iters]
            yield func(*args)
        except StopIteration:
            break

def square(num):
    return num ** 2

# for e in map(lambda a, b: a + b, [1, 2, 3], [4, 5, 6]):
    # print(e)

def add(a, b):
    return a + b

def partial(func, *args):
    def new_func(*more_args):
        all_args = args + more_args
        return func(*all_args)
    return new_func

def caching(func):
    '''Caching deorator'''
    comp_res = {}
    def new_func(*args):
        if args not in comp_res:
            comp_res[args] = func(*args)
        return comp_res[args]
    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    return new_func

@caching
def fib(i):
    if i == 0 or i == 1:
        return 1
    return fib(i - 1) + fib(i - 2)

print(timeit.timeit("fib(30)", number=3,
                    setup="from __main__ import fib"))
