

class Test(object):
    pass


# a = Test()

def logging(self, logmsg):
    print(logmsg)

# Test.__setattr__(logging, logging)

# b = Test()

# print(b.logging("test"))


def bind(instance, func, asname):
    setattr(instance,
            asname,
            func.__get__(instance, instance.__class__))

# Example:


class A:
    pass


a = A()

bind(a, logging, 'logging')
a.logging(":test")
