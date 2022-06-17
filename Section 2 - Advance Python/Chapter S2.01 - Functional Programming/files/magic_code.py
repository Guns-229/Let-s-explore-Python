class XYZ:
    _a = ""

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, val):
        self._a = "Hello " + str(val)


x = XYZ()
x.a = "Mayank"
print(x.a)
x.a = "World"

print(x.a)
