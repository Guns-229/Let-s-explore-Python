
## Python descriptors

Descriptors are similar to Java's `getters`, `setters` & `deletors`. Python provides two ways to achieve it, one is `property` and another is `descriptors`. We have already discussed properties, thus we are going to discuss descriptors in this section.

Python descriptors are used to create `managed attributes`. **Managed Attributes** has many benefits over normal attributes, such as

- Protect attribute value from changing
- Auto updation of depending attributes (e.g. In `circle` object, update in `area` should result in updating of `radius` and vice verses) 
- Custom updation of attribute (e.g. Temperature `C` to `F` or `F` to `C`)

### Descriptors protocol

Any class which implement any of the `__set__`, `__get__` & `__delete__` functions of the class. 

```python
descr.__get__(self, obj, type=None)  #  (returns) value

descr.__set__(self, obj, value)      #  (returns) None

descr.__delete__(self, obj)          #  (returns) None
```

#### Data Descriptors

Descriptor which implement `__get__()` and `__set__()` are called `data descriptors`. They can override the default behavior when called as an attribute. 

#### Non Data Desciptors 

All other descriptors are called `non-data descriptors`. 

### Need of Descriptors

As stated earlier, descriptors are used to implement `managed attributes`. What that means, is using descriptors we can customize an existing or create a custom attribute of the class. With `managed attributes`.

Properties can do lot of the tasks which descriptors can do, what they cannot do is code reuse. They cannot be reused within another class or another property. Descriptors, on the other hand can be used multiple classes or attributes. 

### Creating descriptors

Any class can be converted to descriptor when any of the `__get__()`, `__set__()` or `__delete__()` is implemented. Lets create few descriptors.

#### Creating descriptors using class methods

#### `__set__`

It is used for setting the value of the descriptor. 


```python
class Temprature(object):
    def __init__(self, name):
        self.name = name
        
    def __set__(self, instance, value):
        """
        instance: Obj
        value: <float/int>C / <float/int>F : e.g. 10.2C, 10.2 C, 33.6 F
        """
        print("__set__")
        if value.endswith("c"):
            instance.__dict__[self.name] = (int(value[:-1].strip())* 9/5) + 32
        else:
            instance.__dict__[self.name] = int(value[:-1].strip())
        
class Thermometer(object):
    # Have to do it at Class level and not at object 
    # (so, not at  __init__ )
    temp = Temprature('temp')

    def display(self):
        return self.temp
```


```python
t = Thermometer()
print(t.__dict__)
t.temp = "20c"

print(t.display(), t.temp)
```

    {}
    __set__
    68.0 68.0



```python
t = Thermometer()
print(t.__dict__)
t.temp = "30 F"

print(t.display(), t.temp)
```

    {}
    __set__
    30 30



```python
class Temprature(object):
    def __init__(self, name):
        self.name = name
        
    def __set__(self, instance, value):
        print("__set__")
        if value.endswith("c"):
            instance.__dict__[self.name] = (int(value[:-1])* 9/5) + 32
        else:
            instance.__dict__[self.name] = int(value[:-1])
        
class Thermometer(object):
    # Setting the name to something other than attribute name
    temp = Temprature('temp_in_f')

    def display(self):
        return self.temp

t = Thermometer()
print(t.__dict__)
t.temp = "20c"

print(t.display(), t.temp_in_f)
print(t.__dict__)
```

    {}
    __set__
    <__main__.Temprature object at 0x00000000053153C8> 68.0
    {'temp_in_f': 68.0}



```python
print(dir(t))
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'display', 'temp', 'temp_in_f']


#### `__get__`

It allows to return the value of our custom attribute. We have taken our previous example and implemented the `__get__()`.


```python
class Temprature(object):
    def __init__(self, name):
        self.name = name
        
    def __set__(self, instance, value):
        print("__set__")
        if value.endswith(" c"):
            instance.__dict__[self.name] = (int(value[:-1])* 9/5) + 32
        else:
            instance.__dict__[self.name] = int(value[:-1])
        
    def __get__(self, instance, obj):
#         print(instance, obj)
        print("inside __get__")
        return str(instance.__dict__[self.name]) + " F"
    
    
class Thermometer(object):
    temp = Temprature('temp')

    def display(self):
        return self.temp
    
    def update(self, val):
        self.temp = val
```


```python
t = Thermometer()

t.temp = "20 c"
print("*"*20)
print(t.temp)
```

    __set__
    ********************
    inside __get__
    68.0 F


#### `__delete__`

$$TODO$$


```python
class Temprature(object):
    def __init__(self, name):
        self.name = name
        
    def __set__(self, instance, value):
        print("__set__")
        if value.endswith(" c"):
            instance.__dict__[self.name] = (int(value[:-1])* 9/5) + 32
        else:
            instance.__dict__[self.name] = int(value[:-1])
        
    def __get__(self, instance, obj):
#         print(instance, obj)
        print("inside __get__")
        return str(instance.__dict__[self.name]) + " F"
    
    
class Thermometer(object):
    temp = Temprature('temp')

    def display(self):
        return self.temp
    
    def update(self, val):
        self.temp = val
```


```python
t = Thermometer()

t.temp = "20 c"
print("*"*20)
print(t.display(), t.__dict__)
### !!! ERROR !!!
del(t.temp)
print(t.__dict__())
```

    __set__
    ********************
    inside __get__
    68.0 F {'temp': 68.0}



    -------------------------------------------------------------------------

    AttributeError                          Traceback (most recent call last)

    <ipython-input-32-22b0b964f70d> in <module>()
          5 print(t.display(), t.__dict__)
          6 ### !!! ERROR !!!
    ----> 7 del(t.temp)
          8 print(t.__dict__())


    AttributeError: __delete__

