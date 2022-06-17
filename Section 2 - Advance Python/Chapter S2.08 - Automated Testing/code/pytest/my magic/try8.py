def bread(test_funct):
    def inner(*f,**g):
        print("</''''''\>")
        print(f)
        test_funct(f)
        print("<\______/>")
    return inner


def dec1(func):
    def inner(*args, **kwargs): #1
        print ("dec 1: Arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs) #2
    return inner
    
def dec2(func):
    def inner(*args, **kwargs): #1
        print ("dec 2: Arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs) #2
    return inner

def my_decorator_2(param):
    def actual_decorator(func):
        print("Decorating function {}, with parameter {}".format(func.__name__, param))
        return func  # assume we defined a wrapper somewhere
    return actual_decorator

def my_decorator(param):
    def actual_decorator(func):
        print("Decorating function {}, with parameter {}".format(func.__name__, param))
        return func  # assume we defined a wrapper somewhere
    return actual_decorator


@my_decorator("TEST")
@bread
def test_me(test):
    print("Testing me")
    

test_me("test funct")