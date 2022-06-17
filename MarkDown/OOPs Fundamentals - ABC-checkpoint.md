
# ABC
----
Abstract base classes are a form of interface checking more strict than individual hasattr() checks for particular methods. By defining an abstract base class, you can define a common API for a set of subclasses. This capability is especially useful in situations where a third-party is going to provide implementations, such as with plugins to an application, but can also aid you when working on a large team or with a large code-base where keeping all classes in your head at the same time is difficult or not possible.

## How ABCs Work



```python
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
#     __metaclass__=ABCMeta
    @abstractmethod
    def foo(self):
        pass

#     @abstractmethod
#     def bar(self):
#         pass
    
    def test(self):
        print("TEsT")
    
    
class Concrete(Base):
    def foo(self):
        pass

    # We forget to declare `bar`().

assert issubclass(Concrete, Base)

# b = Base()
c = Concrete()
c.test()
```

    TEsT
    

## Registering the child class
------------


```python
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(object):
    def foo(self):
        print("in child -> foo")
    
    def bar(self):
        print("in child->bar")

Base.register(Concrete)

if __name__ == '__main__':
    print ('Subclass:', issubclass(Concrete, Base))
    print ('Instance:', isinstance(Concrete(), Base))
    c = Concrete()
    c.bar()
```

    Subclass: True
    Instance: True
    in child->bar
    


```python
### Problem
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(object):
    def foo(self):
        print("in child -> foo")
    

Base.register(Concrete)

if __name__ == '__main__':
    print ('Subclass:', issubclass(Concrete, Base))
    print ('Instance:', isinstance(Concrete(), Base))
    c = Concrete()
    c.bar()
```

    Subclass: True
    Instance: True
    


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-4-dbdbb708df16> in <module>()
         23     print ('Instance:', isinstance(Concrete(), Base))
         24     c = Concrete()
    ---> 25     c.bar()
    

    AttributeError: 'Concrete' object has no attribute 'bar'


## Implementation Through Subclassing
----


```python
### Problem
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        print("in child -> foo")
    
    def bar(self):
        print("in child -> bar")
    
    
if __name__ == '__main__':
    print ('Subclass:', issubclass(Concrete, Base))
    print ('Instance:', isinstance(Concrete(), Base))
    c = Concrete()
    c.bar()
```

    Subclass: True
    Instance: True
    in child -> bar
    


```python
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        print("in child -> foo")
    
    def bar(self):
        print("in child->bar")
        
        
if __name__ == '__main__':
    
    print ('Subclass:', issubclass(Concrete, Base))
    print ('Instance:', isinstance(Concrete(), Base))
    c = Concrete()
    c.bar()
```

## Abstract Properties
----
If your API specification includes attributes in addition to methods, you can require the attributes in concrete classes by defining them with @abstractproperty


```python
import abc

class Base(metaclass=ABCMeta):
    
    @abc.abstractproperty
    def value(self):
        return 'Should never get here'


class Implementation(Base):
    @property
    def value(self):
        return 'concrete property'

if __name__ == '__main__':
    try:
        b = Base()
        print ('Base.value:', b.value)
    except Exception as err:
        print ('ERROR:', str(err))

    i = Implementation()
    print ('Implementation.value:', i.value)
```

    ERROR: Can't instantiate abstract class Base with abstract methods value
    Implementation.value: concrete property
    


```python
import abc

class Base(metaclass=abc.ABCMeta):
    
    @abc.abstractproperty
    def value(self):
        return 'Should never see this'
    
    @value.setter
    def value(self, newvalue):
        return


class Implementation(Base):
    
    _value = 'Default value'
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newvalue):
        self._value = newvalue


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


```python

```
