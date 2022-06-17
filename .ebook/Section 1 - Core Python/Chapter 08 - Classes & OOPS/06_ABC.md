
# ABC - Abstract Base Class

Abstract base classes are a form of interface checking more strict than individual `hasattr()` checks for particular methods. By defining an abstract base class, you can define a common API for a set of subclasses. This capability is especially useful in situations where a third-party is going to provide implementations, such as with plugins to an application, but can also aid you when working on a large team or with a large code-base where keeping all classes in your head at the same time is difficult or not possible.

## How ABCs Work



```python
from abc import ABCMeta, abstractmethod


class Mammal(metaclass=ABCMeta):
    ## version 2.x ##     __metaclass__=ABCMeta
    
    @abstractmethod
    def eyes(self, val):
        pass
    
    def hair(self):
        print("hair")
    
    def neocortex(self):
        """a part of the cerebral cortex concerned with sight and hearing in mammals, 
        regarded as the most recently evolved part of the cortex."""
        print("neocortex")
    
class Human(Mammal):
    def eyes(self, val):
        self.eye_color = val
        print("human eyes are {}".format(val))
```


```python
human = Human()
human.eyes("red")
```

    human eyes are red



```python
print(human.__dict__)
```

    {'eye_color': 'red'}



```python
print(dir(human))
```

    ['__abstractmethods__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', 'eye_color', 'eyes', 'hair', 'neocortex']



```python
# Objects of abstract class is not possible
try:
    m = Mammal()
except TypeError as te:
    print(te)
```

    Can't instantiate abstract class Mammal with abstract methods eyes



```python
### !!! Gotcha !!!
class Fish(Mammal):
    pass

try:
    fish = Fish()
except TypeError as te:
    print(te)
```

    Can't instantiate abstract class Fish with abstract methods eyes



```python
class Shark(Fish):
    def eyes(self, val):
        print("Hello, My eyes are {}".format(val))

s = Shark()
s.eyes("green")
```

    Hello, My eyes are green



```python
### !!! Gotcha !!!, To find the reason
class Fish(Mammal):
    pass

def eye(self, val):
    print(val)

try:
    Fish.eyes = eye
    fish = Fish()
except TypeError as te:
    print(te)
```

    Can't instantiate abstract class Fish with abstract methods eyes



```python
# Yes, we can create an abstract class with no abstract attributes, 
# but why will you do it? 

from abc import ABCMeta, abstractmethod


class Mammal(metaclass=ABCMeta):
    pass
```


```python
d = Mammal()
print(d)
```

    <__main__.Mammal object at 0x108699710>



```python
# Yes, you can create a normal class with abstact method,
# !!! Gotcha !!!

class Test(object):
    @abstractmethod
    def test(self):
        print("TEST")
    
t = Test()
t.test()
```

    TEST



```python
print ('Subclass:', issubclass(Human, Mammal))
```

    Subclass: False



```python
print ('Instance:', isinstance(Human(), Mammal))
print ('Instance:', isinstance(human, Mammal))
```

    Instance: False
    Instance: False


** NOTE ** 

* **issubclass**: Return true if class is a subclass (direct, indirect or virtual) of classinfo. A class is considered a subclass of itself. classinfo may be a tuple of class objects, in which case every entry in classinfo will be checked. In any other case, a TypeError exception is raised.

* **isinstance**: Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. Also return true if classinfo is a type object (new-style class) and object is an object of that type or of a (direct, indirect or virtual) subclass thereof. If object is not a class instance or an object of the given type, the function always returns false. If classinfo is a tuple of class or type objects (or recursively, other such tuples), return true if object is an instance of any of the classes or types. If classinfo is not a class, type, or tuple of classes, types, and such tuples, a TypeError exception is raised.

## Registering the child class


```python
from abc import ABCMeta, abstractmethod


class Mammal(metaclass=ABCMeta):
    
    @abstractmethod
    def eyes(self, val):
        raise NotImplementedError()

    def hair(self):
        print("hair")
    
    def neocortex(self):
        """a part of the cerebral cortex concerned with sight and hearing in mammals, 
        regarded as the most recently evolved part of the cortex."""
        print("neocortex")
    
class Human(object):
    def eyes(self, val):
        print("human eyes: ", val)

print ('Subclass:', issubclass(Human, Mammal))        
Mammal.register(Human)
print ('Subclass:', issubclass(Human, Mammal))      
```

    Subclass: False
    Subclass: True



```python
c = Human()
print ('Instance:', isinstance(c, Mammal))
c.eyes("Hazel")
```

    Instance: True
    human eyes:  Hazel


### What is `metaclass`



## Implementation Through Subclassing
----


```python
from abc import ABCMeta, abstractmethod


class Mammal(metaclass=ABCMeta):
## version 2.x ##     __metaclass__=ABCMeta
    
    @abstractmethod
    def eyes(self, val):
        raise NotImplementedError()
    
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
c.eyes("Gray")
```

    Subclass: True
    Instance: True
    Instance: True
    human eyes


### Abstract Method Continued


```python
from abc import ABCMeta, abstractmethod


class Mammal(metaclass=ABCMeta):
## version 2.x ##     __metaclass__=ABCMeta
    
    @abstractmethod
    def eyes(self, color):
        # Partial logic in abstract method
        self.color = color
        print("Eyes color:", self.color)

    def hair(self):
        print("hair")
    
    def neocortex(self):
        """a part of the cerebral cortex concerned with sight and hearing in mammals, 
        regarded as the most recently evolved part of the cortex."""
        print("neocortex")


class Human(Mammal):
    def eyes(self, val):
        print("in human eyes")
        super(Human, self).eyes(val)
        
        # remaining logic
        print("human eyes:", self.color)


print ('Subclass:', issubclass(Human, Mammal))
print ('Instance:', isinstance(Human(), Mammal))
c = Human()
print ('Instance:', isinstance(c, Mammal))
c.eyes("Green")
```

    Subclass: True
    Instance: True
    Instance: True
    in human eyes
    Eyes color: Green
    human eyes: Green


## Abstract Properties
----
`abc` provides `@abstractproperty` decorator to abstract properties.


```python
from abc import ABCMeta, abstractmethod, abstractproperty


class Base(metaclass=ABCMeta):
    
    @abstractproperty
    def value(self):
        return 'Should never get here'


class Implementation(Base):
    @property
    def value(self):
        return 'implemented property'
```


```python
i = Implementation()
print ('Implementation.value:', i.value)
```

    Implementation.value: implemented property



```python
import abc

class Base(metaclass=abc.ABCMeta):
    
    @abc.abstractproperty
    def value(self):
        return 'Should never see this'

class Implementation(Base):
    _value = 'Default value'
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newvalue):
        self._value = newvalue
```


```python
i = Implementation()
print ('Implementation.value:', i.value)

i.value = 'New value'
print ('Changed value:', i.value)
```

    Implementation.value: Default value
    Changed value: New value


#### NOTE #####
For Python 2, that means assigning it to the __metaclass__ attribute on the class:
```python
class CVIterator(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.n = None # the value of n is obtained in the fit method
```
In Python 3, you'd use the metaclass=... syntax when defining the class:
```python
class CVIterator(metaclass=ABCMeta):
    def __init__(self):
        self.n = None # the value of n is obtained in the fit method
```

### The __metaclass__ attribute

The __metaclass__ attribute was introduced to give the programmer some control over the semantics of the class statement
