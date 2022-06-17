
# property 
-----
Python has a great concept called property, which makes the life of an object oriented programmer much simpler. Before defining and going into details of what a property in Python is, let us first build an intuition on why it would be needed in the first place.


```python
CONST = 9/5 # some constant

class Weather_balloon(object):
    def __init__(self, temp):
        self.temp = temp
    
    def convert_temp_to_f(self):
        return self.temp * CONST + 32
    

w = Weather_balloon(122)
print(w.convert_temp_to_f())
```

    251.6



```python
class Circle(object):
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14*radius*radius
```


```python
# Oppppp's !!!!

c = Circle(10)
print(c.radius)

print(c.area)
c.area=222

print(c.radius)
print(c.area)
```

    10
    314.0
    10
    222


### Issue? 

Since they are interdependent attributes, changes one invalidates the other, thus we need to update both at the same time. Properties allows me to achieve it without any issue. 


```python
# Interdepended attributes area & radius

class Circle(object):
    
    def __init__(self, radius):
        self.__set_radius(radius)
        
    def get_area(self):
        return self._area
    
    def __get_radius(self):
        return self.__radius
    
    def __set_radius(self, radius):
        self.__radius = radius
        self._area = 3.14*radius*radius

    radius = property(__get_radius, __set_radius)
```


```python
c = Circle(10)
print(c.radius)
print(c._area)
```

    10
    314.0



```python
c.radius = 100
print(c.radius)
print(c._area)
```

    100
    31400.0



```python
import math

class Circle(object):

    def __init__(self, radius):
        self.__set_radius(radius)
        
    def get_area(self):
        return self.__area
    
    def __get_radius(self):
        return self.__radius
    
    def __set_radius(self, radius):
        self.__radius = radius
        self.__area = 3.14*radius*radius

    radius = property(__get_radius, __set_radius)
    
    @property
    def area(self):
        return self.__area
    
    @area.setter
    def area(self, area):
        self.__area = area
        self.__radius = math.sqrt(self.__area)/3.14
```


```python
c = Circle(101)
print(c.radius)
print(c.area)
```

    101
    32031.14



```python
c.radius = 222

print(c.radius)
print(c.area)
```

    222
    154751.76



```python
c.area=1000

print(c.radius)
print(c.area)
```

    10.070947962319678
    1000



```python
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
```


```python
man = Celsius()
# set temperature
man.temperature = 37

# get temperature
print(man.temperature)


# get degrees Fahrenheit
print(man.to_fahrenheit())
##### print(Celsius.temperature)
```

    37
    98.60000000000001



```python
##############
### Riddle ###
##############
class MyClass(): 
    x = 0
    y = 100

a = MyClass()
b = MyClass()

a.x = 2
print(id(a.y), id(b.y))
print(id(a.x), id(b.x))
print(b.x)

MyClass.x = 4
print(a.x)
print(b.x)

MyClass.x = 7
print(a.x)
print(b.x)
print("~~~~~~")
b.x = MyClass.y
MyClass.x = 4
print(b.x)
```

    4450346896 4450346896
    4450343760 4450343696
    0
    2
    4
    2
    7
    ~~~~~~
    100


## Class with Getter and Setter


```python
class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
```

We can see above that new methods get_temperature() and set_temperature() were defined and furthermore, temperature was replaced with \_temperature. An underscore (\_) at the beginning is used to denote private variables in Python.

## Python Way - Property
----
The pythonic way to deal with the above problem is to use property. Here is how we could have achieved it.


```python
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)
```


```python
man = Celsius()
# set temperature
man.temperature = 137

# get temperature
print(man.temperature)

# get degrees Fahrenheit
print(man.to_fahrenheit())
##### print(Celsius.temperature)
```

    Setting value
    Setting value
    Getting value
    137
    Getting value
    278.6


## Deep in Property

- Method 1
```python
temperature = property(get_temperature, set_temperature)
```

-  Method 2
```python
# make empty property
temperature = property()
# assign getter
temperature = temperature.getter(get_temperature)
# assign setter
temperature = temperature.setter(set_temperature)
```

- Method 3

```python
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


celc = Celsius()
celc.temperature = 100
print(celc.temperature)
# del(celc.temperature) # Need to explicitly define a deleter
# print(celc.temperature)
```

Another example to 


```python
### Method 3
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
        
    @temperature.deleter
    def temperature(self):
        print("deleting the property")
        del(self._temperature)
```


```python
celc = Celsius()
celc.temperature = 100
print(celc.temperature)
del(celc.temperature)
try:
    print(celc.temperature) # This property is no longer valid thus will error out
except Exception as e:
    print(e)
```

    Setting value
    Getting value
    100
    deleting the property
    Getting value
    'Celsius' object has no attribute '_temperature'

