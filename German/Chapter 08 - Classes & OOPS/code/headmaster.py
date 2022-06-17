class HeadMaster(object):
    __instances = []  # Keep track of instance reference
    __limit = 2

    def __new__(cls, *args, **kwargs):
        if len(cls.__instances) >= cls.__limit:
            raise RuntimeError("Creation Limit %s reached" % cls.__limit)
        
        instance = object.__init__(cls)
        cls.__instances.append(instance)
        return instance
    
    def __init__(self, name):
        self.name = name

    def __del__(self):
        self.__instance.remove(self)

try:
    li1 = HeadMaster("Gupta Sir")
    # print(li1.name)
    li2 = HeadMaster("Sharma Sir")
    # print(li.name)
    print("2 object created ")
    li3 = HeadMaster("Tiwari Sir")
    print("3 object created ")
    li4 = HeadMaster()
except Exception as e:
    print("Exception:", e)
