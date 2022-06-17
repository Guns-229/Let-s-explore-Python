class CustomException(BaseException):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


def createInstance():
    # Do what ever you want to determie if instance can be created
    global flg
    flg != flg
    return flg


class CustomizeInstance(object):

    def __new__(cls, a, b):
        if not createInstance():
            return None
        instance = super(CustomizeInstance, cls).__new__(cls)
        instance.a = a
        return instance

    def __init__(self, a, b):
        pass


flg = False
d = CustomizeInstance(1, 2)
a = CustomizeInstance(2, 3)
