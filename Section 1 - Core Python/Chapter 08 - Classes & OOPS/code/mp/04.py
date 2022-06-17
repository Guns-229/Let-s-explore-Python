class Ram(object):
    pass

class Kush(Ram):
    pass

def chant(cls):
    print("... Ohm ...")

kush = Kush()
print('chant' in kush.__dir__())

Ram.chant = chant
love = Kush()

love.chant()
kush.chant()
print('chant' in kush.__dir__())
print('chant' in love.__dir__())
