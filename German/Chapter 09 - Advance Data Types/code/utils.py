import time

def speed_test(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        for x in range(5000):
            results = func(*args, **kwargs)
        t2 = time.time()
        print(('%s took %0.3f ms' %
               (func.__name__, (t2-t1)*1000.0)))
        return results
    return wrapper

@speed_test
def compare_bitwise(x, y):
    set_x = frozenset(x)
    set_y = frozenset(y)
    return set_x & set_y

@speed_test
def compare_listcomp(x, y):
    return [i for i, j in zip(x, y) if i == j]

@speed_test
def compare_intersect(x, y):
    fx = frozenset(x)
    return fx.intersection(y), fx.difference(y)
