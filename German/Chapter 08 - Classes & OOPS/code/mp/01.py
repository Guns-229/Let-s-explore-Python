class Hanuman(object):
    pass

def chant(cls):
    print("Jai Jai Shri Ram")

heman = Hanuman()
print('chant' in heman.__dir__())

Hanuman.chant = chant

hanuman = Hanuman()
hanuman.chant()

print('chant' in heman.__dir__())
print('chant' in hanuman.__dir__())

