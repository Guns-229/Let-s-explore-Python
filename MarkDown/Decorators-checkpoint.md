
# Decorators
---
## ONLY AFTER FP
A decorator is the name used for a software design pattern. Decorators dynamically alter the functionality of a function, method, or class without having to directly use subclasses or change the source code of the function being decorated.

Python decorator is a specific change to the Python syntax that allows us to more conveniently alter functions and methods (and possibly classes in a future version). This supports more readable applications of the DecoratorPattern but also other uses as well.


```python
def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper

def sandwich(food="--ham--"):
    print(food)

# sandwich()
test = bread(ingredients(sandwich))
test()
```

    </''''''\>
    #tomatoes#
    --ham--
    ~salad~
    <\______/>
    


```python
@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)

sandwich()
```

    </''''''\>
    #tomatoes#
    --ham--
    ~salad~
    <\______/>
    

> ***!!! Order Matters !!!*** 


```python
@ingredients
@bread
def sandwich(food="--ham--"):
    print(food)

sandwich()
```

    #tomatoes#
    </''''''\>
    --ham--
    <\______/>
    ~salad~
    


```python
@bread
@ingredients
def hotdog(food="tuna"):
    print(food)

hotdog()
```

    </''''''\>
    #tomatoes#
    tuna
    ~salad~
    <\______/>
    


```python

```

## Bound methods
---

Unless you tell it not to, Python will create what is called a bound method when a function is an attribute of a class and you access it via an instance of a class. This may sound complicated but it does exactly what you want.


```python
class A(object):
    def method(*argv):
        return argv
a = A()
a.method

```




    <bound method A.method of <__main__.A object at 0x00000234D70DB8D0>>




```python
a.method('an arg')
```




    (<__main__.A at 0x234d70db8d0>, 'an arg')



### staticmethod()

A static method is a way of suppressing the creation of a bound method when accessing a function.


```python
class A(object):
    @staticmethod
    def method(*argv):
        return argv
a = A()
a.method
```




    <function __main__.A.method>



When we call a static method we don’t get any additional arguments.


```python
a.method('an arg')
```




    ('an arg',)



### classmethod

A class method is like a bound method except that the class of the instance is passed as an argument rather than the instance itself.


```python
class A(object):
    @classmethod
    def method(*argv):
        return argv
a = A()
a.method
```




    <bound method A.method of <class '__main__.A'>>




```python
a.method('an arg')
```




    (__main__.A, 'an arg')


