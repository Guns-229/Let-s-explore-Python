## Patching existing function
class Hanuman(object):
    def chant(self, padding="****"):
        print(" __ Jai Jai Shri Ram __")
        print(padding)

def chant(cls):
    print("Jai Jai Shri Ram", cls.padding)

heman = Hanuman()
heman.chant()
print('padding' in heman.__dir__())

Hanuman.chant = chant
hanuman = Hanuman()
Hanuman.padding = "$$$"

hanuman.chant()
heman.chant()
print('padding' in heman.__dir__())
print('padding' in hanuman.__dir__())
