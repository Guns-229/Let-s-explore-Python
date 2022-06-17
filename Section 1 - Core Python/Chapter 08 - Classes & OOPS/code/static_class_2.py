class A(object):
    x = 0
    def foo(self,x):
        self.x = x
        print("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        cls.x = x
        print("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)

a=A()
a.foo(1)
a.class_foo(2)
a.static_foo(3)
