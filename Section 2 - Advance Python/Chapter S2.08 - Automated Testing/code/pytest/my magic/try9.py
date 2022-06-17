
def bread(test_funct):
    def inner(*f, **g):
        print("</''''''\>")
        print(f)
        print(test_funct)
        print("<\______/>")
    return inner


def dec1(func):
    def inner(*args, **kwargs):
        print("dec 1: Arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs)
    return inner


def dec2(func):
    def inner(*args, **kwargs):
        print("dec 2: Arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs)
    return inner


def my_decorator_2(param):
    def actual_decorator(func):
        print("Decorating function {}, with parameter {}".format(func.__name__,
                                                                 param))
        return func  # assume we defined a wrapper somewhere
    return actual_decorator


def my_decorator(param):
    def actual_decorator(func):
        print("Decorating function {}, with parameter {}".format(func.__name__,
                                                                 param))
        return func  # assume we defined a wrapper somewhere
    return actual_decorator


@bread("DDD")
@my_decorator("TEST")
def test_me(test):
    print("Testing me")


def test():
    print("Hello ")


test_me("test funct")
