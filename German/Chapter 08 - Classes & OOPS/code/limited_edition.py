class CustomException(BaseException):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


class LimitedInstances(object):
    _instances = []  # Keep track of instance reference
    limit = 2

    def __new__(cls, *args, **kwargs):
        print("inside __new__", len(cls._instances), cls.limit)

        instance = object.__new__(cls)
        cls._instances.append(instance)
        print("still inside __new__")
        return instance

    def __init__(self, *args, **kwargs):
        self._inst = len(self._instances) + 1
        print("inside __init__", len(self._instances), self.limit)
        if len(self._instances) >= self.limit:
            self._Errorflg = True
            raise CustomException("test")

    def __del__(self):
        print("inside __del__", self.__dict__.get("_Errorflg", self._inst),
              flush=True)
        # Remove instance from _instances
        if not self.__dict__.get("_Errorflg"):
            self._instance.remove(self)


li1 = LimitedInstances()
li2 = LimitedInstances()
try:
    li3 = LimitedInstances()
except Exception as e:
    print(e)
