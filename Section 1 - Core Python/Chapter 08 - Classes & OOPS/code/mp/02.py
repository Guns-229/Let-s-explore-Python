## Patching a new variable
class Hanuman(object):
    def chant(self):
        print(" __ Jai Jai Shri Ram __")

def chant(cls):
    print("Jai Jai Shri Ram")

heman = Hanuman()
heman.chant()

Hanuman.chant = chant

hanuman = Hanuman()
hanuman.chant()
heman.chant()

