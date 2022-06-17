class HeadMaster(object):
    _instances = []  # Keep track of instance reference
    limit = 2

    def __new__(cls, *args, **kwargs):
        if len(cls._instances) >= cls.limit:
            raise RuntimeError("Creation Limit %s reached" % cls.limit)
        instance = object.__init__(cls)
        cls._instances.append(instance)
        return instance

    def __del__(self):
        # Remove instance from _instances
        self._instance.remove(self)

try:
    li1 = HeadMaster()
    li2 = HeadMaster()
    li3 = HeadMaster()
    li4 = HeadMaster()
except Exception as e:
    print(e)
