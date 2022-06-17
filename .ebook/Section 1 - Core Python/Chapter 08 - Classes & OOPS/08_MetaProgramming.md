
# Metaprogramming
-----
Objects are created by other objects: special objects called “classes” that we can set up to spit out objects that are configured to our liking.

Classes are just objects, and they can be modified the same way:


```python
class Foo(object): pass

print(type(Foo))
```

    <class 'type'>



```python
class Foo(object): pass

Foo.field = 42

x = Foo()
x.field
```




    42




```python
print(Foo.field)
```

    42



```python
x.field = 22
print(x.field)
print(Foo.field)
```

    22
    42



```python
# Auto object updation, I updated the class attribute and object attribute got updated

Foo.field2 = 99
print(x.field2)
```

    99



```python
# Once object start pointing to another memory location, it will not get updated.

Foo.field = 122
print(x.field)
print(Foo.field)
```

    22
    122



```python
Foo.method = lambda self: "Hi!"
x.method()
```




    'Hi!'



To modify a class, you perform operations on it like any other object. You can add and subtract fields and methods, for example. The difference is that any change you make to a class affects all the objects of that class, even the ones that have already been instantiated.

What creates these special “class” objects? Other special objects, called metaclasses.

The default metaclass is called type and in the vast majority of cases it does the right thing. In some situations, however, you can gain leverage by modifying the way that classes are produced – typically by performing extra actions or injecting code. When this is the case, you can use metaclass programming to modify the way that some of your class objects are created.

It’s worth re-emphasizing that in the vast majority of cases, you don’t need metaclasses, because it’s a fascinating toy and the temptation to use it everywhere can be overwhelming. Some of the examples in this chapter will show both metaclass and non-metaclass solutions to a problem, so you can see that there’s usually another (often simpler) approach.

Some of the functionality that was previously only available with metaclasses is now available in a simpler form using class decorators. It is still useful, however, to understand metaclasses, and certain results can still be achieved only through metaclass programming.

## Basic Metaprogramming
-----

So metaclasses create classes, and classes create instances. Normally when we write a class, the default metaclass type is automatically invoked to create that class, and we aren’t even aware that it’s happening.

It’s possible to explicitly code the metaclass’ creation of a class. type called with one argument produces the type information of an existing class; type called with three arguments creates a new class object. The arguments when invoking type are the name of the class, a list of base classes, and a dictionary giving the namespace for the class (all the fields and methods). So the equivalent of:


```python
class C: pass
```


```python
print(C)
```

    <class '__main__.C'>


is


```python
CMeta = type('C', (), {})
```


```python
print(CMeta)
```

    <class '__main__.C'>



```python
class Cpp(object):
    """This is a doc"""
    def me(self):
        self.meme="Me"
    
    def you(self):
        self.youyou = "You"
```


```python
print(type(Cpp))
print(Cpp.__dict__)
```

    <class 'type'>
    {'__module__': '__main__', '__doc__': 'This is a doc', 'me': <function Cpp.me at 0x108835710>, 'you': <function Cpp.you at 0x1088357a0>, '__dict__': <attribute '__dict__' of 'Cpp' objects>, '__weakref__': <attribute '__weakref__' of 'Cpp' objects>}



```python
cpp = Cpp()
cpp.me()
print(cpp.meme)
```

    Me


Lets create a meta class 


```python
def me(self):
    self.meme="Me"

def you(self):
    self.youyou = "You"

Cpp = type('Cpp', (), dict(me=me, you=you))
```


```python
print(type(Cpp))
print(Cpp.__dict__)
```

    <class 'type'>
    {'me': <function me at 0x1088358c0>, 'you': <function you at 0x108835680>, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Cpp' objects>, '__weakref__': <attribute '__weakref__' of 'Cpp' objects>, '__doc__': None}



```python
cpp = Cpp()
cpp.me()
print(cpp.meme)
```

    Me


Classes are often referred to as “types,” so this reads fairly sensibly: you’re calling a function that creates a new type based on its arguments.

We can also add base classes, fields and methods:


```python
# Original Class
class MyList(list):
    x = 42
    def howdy(self, you):
        print("Howdy,", you)
```


```python
ml = MyList()
ml.append("Camembert")
print(ml)
print(ml.x)
ml.howdy("John")
```

    ['Camembert']
    42
    Howdy, John



```python
# Meta class version
def howdy(self, you):
    print("Howdy,", you)

MyList = type('MyList', (list,), dict(x=42, howdy=howdy))
```


```python
ml = MyList()
ml.append("Camembert")
print(ml)
print(ml.x)
ml.howdy("John")
```

    ['Camembert']
    42
    Howdy, John


Note that printing the class of the class produces the metaclass.

The ability to generate classes programmatically using type opens up some interesting possibilities.
