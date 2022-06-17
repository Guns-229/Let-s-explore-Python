class SingletonError(Exception):
    pass


class HeadMaster(object):

    def __new__(cls, name):
        it = cls.__dict__.get("__it__")
        if it is not None:
            raise SingletonError("Count not create new instance. %s", name)

        cls.__it__ = it = object.__new__(cls)
        it.__init__(name)
        return it

    def print_name(self):
        print(self.name)


try:
    anshu_mam = HeadMaster("Anshu Shrivastava")
    rahim_sir = HeadMaster("Rahim Khan")
except Exception as e:
    print(e)
