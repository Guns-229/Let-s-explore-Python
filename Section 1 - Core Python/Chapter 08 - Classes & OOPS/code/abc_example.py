from abc import ABCMeta, abstractmethod


class Mammal(metaclass=ABCMeta):
## version 2.x ##     __metaclass__=ABCMeta

    @abstractmethod
    def eyes(self, val):
        pass

#     @abstractmethod
#     def hand(self):
#         pass

    def hair(self):
        print("hair")

    def neocortex(self):
        """a part of the cerebral cortex concerned with sight and hearing in mammals,
        regarded as the most recently evolved part of the cortex."""
        print("neocortex")

class Human(Mammal):
    def eyes(self, val):
        print("human eyes")

print ('Subclass:', issubclass(Human, Mammal))
print ('Instance:', isinstance(Human(), Mammal))
c = Human()
print ('Instance:', isinstance(c, Mammal))
c.eyes("red")
