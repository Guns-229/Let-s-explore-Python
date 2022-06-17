
# `_`, `__` and `__attr__` in Python

Certain classes of identifiers (besides keywords) have special meanings. These classes are identified by the patterns of leading and trailing underscore characters:

`_*`
Not imported by "from module import *". The special identifier "`_`" is used in the interactive interpreter to store the result of the last evaluation; it is stored in the `__builtin__` module. When not in interactive mode, "`_`" has no special meaning and is not defined. See section 6.12, ``The import statement.''
Note: The name "_" is often used in conjunction with internationalization; refer to the documentation for the gettext module for more information on this convention.

`__*__`
System-defined names. These names are defined by the interpreter and its implementation (including the standard library); applications should not expect to define additional names using this convention. The set of names of this class defined by Python may be extended in future versions. See section 3.4, ``Special method names.''

`__*`
Class-private names. Names in this category, when used within the context of a class definition, are re-written to use a mangled form to help avoid name clashes between **private** attributes of **base** and **derived** classes.


```python
# Static function
class SumTotal(object):
    init_no = [10]
    
    def __init__(self):
        self.actual = 100
        pass
    
    @staticmethod
    def static_method(nums):
        # They have no access to object/class attributes
        print(nums)
    
    @classmethod
    def cls_method(cls):
        print(cls.init_no)
        # As class methods do not have access to object attributes
        try:
            print(cls.actual)
        except Exception as e:
            print(e)
        

st = SumTotal()
st.static_method(1010)

st.cls_method()
SumTotal.static_method(22)
```

    1010
    [10]
    type object 'SumTotal' has no attribute 'actual'
    22



```python
# Explicitly calling parent function

class Base(object):
    def test(self, data):
        print("data: {}".format(data))
        
class Child(Base):
    def test(self, data):
        super().test(data)
        
c = Child()
c.test("testing")
```

    data: testing


### Monkey Patching of Classes

Below is a very simple example of monkey patching of classes in Python. 
> **Note**
> ____
>After patching, all the object created will get the updates irrespective of when they were created as shown in the below example. 


```python
# mp/01.py
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
```

    False
    Jai Jai Shri Ram
    True
    True



```python
## Patching a new variable
# mp/02.py

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
```

     __ Jai Jai Shri Ram __
    Jai Jai Shri Ram
    Jai Jai Shri Ram



```python
## Patching existing function
# mp/03.py
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
```

     __ Jai Jai Shri Ram __
    ****
    False
    Jai Jai Shri Ram $$$
    Jai Jai Shri Ram $$$
    True
    True


### Effects of patching Parent Class on child objects


```python
# mp/04.py
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
```

    False
    ... Ohm ...
    ... Ohm ...
    True
    True

