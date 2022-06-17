
# Composition
-----
Inheritance is useful, but another way to do the exact same thing is just to use other classes and modules, rather than rely on implicit inheritance. If you look at the three ways to exploit inheritance, two of the three involve writing new code to replace or alter functionality. This can easily be replicated by just calling functions in a module. Here's an example of doing this:


```python
class Spa(object):
    def __init__(self):
        print("in init of spa")
        
    def usage(self):
        print("in spa usage")

class CoffeeShop(object):
    def __init__(self):
        print("in init of coffeeshop")
        
    def usage(self):
        print("in CoffeeShop usage")
        
class Laundery(object):
    def __init__(self):
        print("in init of Laundery")
    
    def usage(self):
        print("in Laundery usage")

class Hotel(object):
    def __init__(self):
        print("Hotel init")
        self.spa = Spa()
        self.cs = CoffeeShop()
        self.laundery = Laundery()
```


```python
h = Hotel()
print("~^"*10)
h.spa.usage()
h.laundery.usage()
```

    Hotel init
    in init of spa
    in init of coffeeshop
    in init of Laundery
    ~^~^~^~^~^~^~^~^~^~^
    in spa usage
    in Laundery usage



```python
class Other():        
    def test(self):
        print("Test")


class Child():
    x = 12
    def __init__(self):
        Child.other = Other()

    def implicit(self):
        self.x = 11
        self.other.test()

son = Child()
girl = Child()

son.other.test()
girl.implicit()
print(girl.x, son.x)
```

    Test
    Test
    11 12



```python
# Effect on static immutable data
# Since the `other` is a class object any change in attributes of it 
# will get reflected in all objects

class Other():
    a = 10

    def test(self):
        print("Test")

class Child():
    x = 12
    def __init__(self):
        # Class level object, all the objects will share it.
        Child.other = Other()

    def implicit(self):
        self.x = 11
        self.other.test()

son = Child()
girl = Child()
son.other.a = 1100

son.implicit()
print("girl.other.a:", girl.other.a)
print(id(son.other), id(girl.other))
```

    Test
    girl.other.a: 1100
    4456235344 4456235344



```python
# Effect on static immutable data
# Since the `other` is a class object any change in attributes of it 
# will get reflected in all objects

class Other():
    def __init__(self):
        self.a = 100

    def test(self):
        print(f"Test: {self.a}")

class Child():
    x = 12
    def __init__(self):
        # Class level object, all the objects will share it.
        Child.other = Other()

    def implicit(self):
        self.x = 11
        self.other.test()

son = Child()
girl = Child()
son.other.a = 1100

son.implicit()
print("girl.other.a:", girl.other.a)
print(id(son.other), id(girl.other))
```

    Test: 1100
    girl.other.a: 1100
    4456238416 4456238416



```python
class Other():
    a = 10

    def test(self):
        print("Test")


class Child():
    x = 12
    def __init__(self):
        # Object level object, every Child object will have 
        # different `other` object.
        self.other = Other()

    def implicit(self):
        self.x = 11
        self.other.test()

son = Child()
girl = Child()
son.other.a = 1100

son.implicit()
print(girl.other.a)
print(id(son.other), id(girl.other))
```

    Test
    10
    4456264784 4456264976


## When to Use Inheritance or Composition

The question of "inheritance versus composition" comes down to an attempt to solve the problem of reusable code. You don't want to have duplicated code all over your software, since that's not clean and efficient. Inheritance solves this problem by creating a mechanism for you to have implied features in base classes. Composition solves this by giving you modules and the ability to call functions in other classes.

If both solutions solve the problem of reuse, then which one is appropriate in which situations? The answer is incredibly subjective, but I'll give you my three guidelines for when to do which:

* Avoid multiple inheritance at all costs, as it's too complex to be reliable. If you're stuck with it, then be prepared to know the class hierarchy and spend time finding where everything is coming from.
* Use composition to package code into modules that are used in many different unrelated places and situations.
* Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you're using.

Do not be a slave to these rules. The thing to remember about object-oriented programming is that it is entirely a social convention programmers have created to package and share code. Because it's a social convention, but one that's codified in Python, you may be forced to avoid these rules because of the people you work with. In that case, find out how they use things and then just adapt to the situation.
