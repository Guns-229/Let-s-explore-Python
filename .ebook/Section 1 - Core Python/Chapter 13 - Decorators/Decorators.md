
# Decorators

## Introduction

A decorator is the name used for a software design pattern. Decorators dynamically alter the functionality of a function, method, or class without having to directly use subclasses or change the source code of the function being decorated.

Python decorator is a specific change to the Python syntax that allows us to more conveniently alter functions and methods (and possibly classes in a future version). This supports more readable applications of the DecoratorPattern but also other uses as well.


```python
def bread(test_funct):
    def hyderabad(c=""):
        print("</''''''\>")
        test_funct(c)
        print("<\______/>")
    return hyderabad

def ingredients(test_funct):
    def chennai(c=""):
        print("#tomatoes#")
        test_funct(c)
        print("~salad~")
    return chennai

def cheese(food="--Say Cheese--"):
    print(food)

```


```python
ch = bread(cheese)
print(ch)
print("...")
ch1 = bread(cheese)
print(ch1)
```

    <function bread.<locals>.hyderabad at 0x108b1a290>
    ...
    <function bread.<locals>.hyderabad at 0x108b1a560>



```python
ch("Egg Plant")
```

    </''''''\>
    Egg Plant
    <\______/>



```python
inn = bread(ingredients(cheese))
inn("Potato Chips")
```

    </''''''\>
    #tomatoes#
    Potato Chips
    ~salad~
    <\______/>



```python
inn = ingredients(bread(cheese))
inn("Potato Chips")
```

    #tomatoes#
    </''''''\>
    Potato Chips
    <\______/>
    ~salad~


## Function Decorators

A function decorator is applied to a function definition by placing it on the line before that function definition begins


```python
@bread
@ingredients
def sandwich(food="--Say Cheese--"):
    print(food)

sandwich("Potato Chips")
```

    </''''''\>
    #tomatoes#
    Potato Chips
    ~salad~
    <\______/>


> ***!!! Order Matters !!!*** 


```python
@ingredients
@bread
def sandwich(food="--Say Cheese--"):
    print(food)

sandwich("Kashimiri Mirch")
```

    #tomatoes#
    </''''''\>
    Kashimiri Mirch
    <\______/>
    ~salad~



```python
def hotdog(food="Jam"):
    print(food)

hotdog()
```

    Jam



```python
@bread
@ingredients
def hotdog(food):
    print(food)

hotdog("Jam")
```

    </''''''\>
    #tomatoes#
    Jam
    ~salad~
    <\______/>



```python
def sandwich(food="--Say Cheese--"):
    print(food)

sandwich("Yummy")
```

    Yummy



```python
# By omiting the `inner_funct in `inner`, I am making sure that my decorated 
# function is very called. 

def diet_sandwitch(inner_func):
    def inner(c):
        print("salad")
    return inner

@bread
@diet_sandwitch
@ingredients
def sandwich(food="--Say Cheese--"):
    print(food)

sandwich("Yummy")
```

    </''''''\>
    salad
    <\______/>


## Decorators with arguments

### Using Functions

We can create a function which can take an argument and wrap the original decorator inside as shown in below code sample.


```python
def corps_fun(*deco_args, **deco_kwargs):
    def real_decorator(func):
        def inner(*args, **kwargs):
            print("inside inner args:", deco_args)
            for k, v in deco_kwargs.items():
                print("inside inner kwars:", k, v)
            print(*args, kwargs)
            func(*args, **kwargs)
        return inner
    return real_decorator


@corps_fun("arg1", "arg2")
def print_args(*args, **kwargs):
    print("TEST")
    for arg in args:
        print("arg", arg)
    for k, v in kwargs.items():
        print("kwargs", k, v)
```


```python
print_args(1, 2, 3, corp="Bhopal Municipal Corporation")
```

    inside inner args: ('arg1', 'arg2')
    1 2 3 {'corp': 'Bhopal Municipal Corporation'}
    TEST
    arg 1
    arg 2
    arg 3
    kwargs corp Bhopal Municipal Corporation



```python
def decorator(*deco_args, **deco_kwargs):
    def real_decorator(func):
        def inner(*args, **kwargs):
            print("inside inner args:", args)
            print("inside inner kwargs:", kwargs)
            # Calling the actual function
            func(*args, **kwargs)
        return inner
    return real_decorator


@decorator("arg1", "arg2")
def print_args(*args, **kwargs):
    print("TEST")
    for arg in args:
        print("arg", arg)
    for k, v in kwargs.items():
        print("kwargs", k, v)
```


```python
print_args(1, 2, 3, corp="Bhopal Municipal Corporation")
```

    inside inner args: (1, 2, 3)
    inside inner kwargs: {'corp': 'Bhopal Municipal Corporation'}
    TEST
    arg 1
    arg 2
    arg 3
    kwargs corp Bhopal Municipal Corporation



```python
@decorator("arg1", "arg2", ver="10.2.301")
def print_args(*args, **kwargs):
    print("TEST")
    for arg in args:
        print("arg", arg)
    for k, v in kwargs.items():
        print("kwargs", k, v)
```


```python
print_args(1, 2, 3, corp="Bhopal Municipal Corporation")
```

    inside inner args: (1, 2, 3)
    inside inner kwargs: {'corp': 'Bhopal Municipal Corporation'}
    TEST
    arg 1
    arg 2
    arg 3
    kwargs corp Bhopal Municipal Corporation



```python
def decorator(*deco_args, **deco_kwargs):
    def real_decorator(func):
        def inner(*args, **kwargs):
            print("inside inner args:", args)
            print("inside inner kwargs:", kwargs)
            # Calling the actual function
            if args[0] == 0:
                func(*args, **kwargs)
        return inner
    return real_decorator


@decorator("arg1", "arg2")
def print_args(*args, **kwargs):
    print("TEST")
    for arg in args:
        print("arg", arg)
    for k, v in kwargs.items():
        print("kwargs", k, v)
```


```python
print_args(1, 2, 3, corp="Bhopal Municipal Corporation")
```

    inside inner args: (1, 2, 3)
    inside inner kwargs: {'corp': 'Bhopal Municipal Corporation'}



```python
print_args(0, 1, 2, 3, corp="Bhopal Municipal Corporation")
```

    inside inner args: (0, 1, 2, 3)
    inside inner kwargs: {'corp': 'Bhopal Municipal Corporation'}
    TEST
    arg 0
    arg 1
    arg 2
    arg 3
    kwargs corp Bhopal Municipal Corporation


In the above example, we bypassed the execution of actual function itself.

### Limitations 

$$TODO$$

We can obtain the same using the `wrapper` function of functools


```python
from functools import wraps

def decorator(*deco_args, **deco_kwargs):
    method_or_name = deco_args
    
    def real_decorator(method):    
        if callable(method_or_name):
            print("if", method_or_name)
            method.gw_method = method.__name__
        else:
            print("Else", method_or_name)
            method.gw_method = method_or_name

        @wraps(method)
        def wrapper(*args, **kwargs):
            method(*args, **kwargs)
        return wrapper
    if callable(method_or_name):
        return real_decorator(method_or_name)
    return real_decorator

@decorator("arg1", "arg2", test="test")
def print_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, v)

print_args(1, 2, 3, d="Satyam")
```

    Else ('arg1', 'arg2')
    1
    2
    3
    d Satyam



```python

```

#### Conditional Decorators

There are scenarios were we want to run the decorators only under certain condition, although Python do not natively support it, but we can achieve it with the following code template.


```python
def condition(**deco_kwargs):
    
    def __decorator__(func):
    
        def __inner__(*args, **kwargs):
            if deco_kwargs.get('flag', False):
                return func(*args, **kwargs)
            
        return __inner__
    return __decorator__
        

def decorator(func):
    def inner(*args, **kwargs):
        print("Yadayada _ in inner")
        print(*args, **kwargs)
        print(args)
        for k, v in kwargs.items():
            print(k, v)
        func(*args, **kwargs)
    return inner

debug = False

@condition(flag=debug)
@decorator
def print_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, v)


print_args(1, 2)
print("...done....")
```

    ...done....



```python
debug = True
def condition(**deco_kwargs):
    def __decorator__(func):
        def __inner__(*args, **kwargs):
            if deco_kwargs.get('flag', False):
                return func(*args, **kwargs)
#             return func(*args, **kwargs)
        return __inner__
    return __decorator__
        

def decorator(func):
    def inner(*args, **kwargs):
        print("Yadayada _ in inner")
        print(*args, **kwargs)
        print(args)
        for k, v in kwargs.items():
            print(k, v)
        func(*args, **kwargs)
    return inner

@condition(flag=debug)
@decorator
def print_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, v)


print_args(1, 2)
```

    Yadayada _ in inner
    1 2
    (1, 2)
    1
    2


### Context Managers as Decorators 

Context managers can also be used as decorators, as shown below (https://docs.python.org/dev/library/contextlib.html#contextlib.ContextDecorator)


```python
from contextlib import ContextDecorator

class mycontext(ContextDecorator):
    def __enter__(self):
        print('Starting')
        return self

    def __exit__(self, *exc):
        print('Finishing')
        return False

@mycontext()
def function():
    print('The bit in the middle')
```


```python
function()
```

    Starting
    The bit in the middle
    Finishing



```python
def function_2():
    print("This is function 2")
    
with mycontext() as t: 
    function_2()
```

    Starting
    This is function 2
    Finishing



```python
from contextlib import ContextDecorator

class mycontext(ContextDecorator):
    def __enter__(self):
        print('Starting')
        return self

    def __exit__(self, *exc):
        print('Finishing')
        return False

@mycontext()
def function():
    raise Exception("Raising Error")
    print('The bit in the middle')

try:
    function()
except Exception as e:
    print("Error:", e)
```

    Starting
    Finishing
    Error: Raising Error


In the above example, although the exception was not handled, yet, `__end__` funtion was called by python

## Class Decorators


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




    <bound method A.method of <__main__.A object at 0x108b1f990>>




```python
a.method('an arg')
```




    (<__main__.A at 0x108b1f990>, 'an arg')



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




    <function __main__.A.method(*argv)>



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




```python
def test(strg):
    print("Name: ", strg)
    
def hello(func, name):
    print("Ja")
    func(name)
    
hello(test, "Mayank")
```

    Ja
    Name:  Mayank



```python
class B(object):
    @classmethod
    def method(*argv):
        return argv
```


```python
a = B()
a.method()
```




    (__main__.B,)



## References:

- https://www.python.org/dev/peps/pep-0318/
