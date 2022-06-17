
# OOPS Fundamentals 
----
## What is Inheritance?

Inheritance is used to indicate that one class will get most or all of its features from a parent class. This happens implicitly whenever you write class Foo(Bar), which says "Make a class Foo that inherits from Bar." When you do this, the language makes any action that you do on instances of Foo also work as if they were done to an instance of Bar. Doing this lets you put common functionality in the Bar class, then specialize that functionality in the Foo class as needed.

When you are doing this kind of specialization, there are three ways that the parent and child classes can interact:

* Actions on the child imply an action on the parent.
* Actions on the child override the action on the parent.
* Actions on the child alter the action on the parent.

Also to note:

- **Implicit Inheritance**: when you define a function in the parent, but not in the child. 
- **Override Explicitly**: when you define a function in the parent, and also in the child. 


```python
# Example 1:
class Parent(object):
    def __init__(self):
        print("Parent init")
    
class Child(Parent):
    def __init__(self):
        print("Child init")

child = Child()
```

    Child init



```python
# Example 2:
class Parent(object):
    def __init__(self):
        print("Parent init")

class Child(Parent):
    pass
        

child = Child()
```

    Parent init



```python
class Parent(object):
    def __init__(self):
        print("Parent init")

    def override(self):
        print( "PARENT override()")

    def implicit(self):
        print ("PARENT implicit()")


class Child(Parent):
    def __init__(self):
        print("Child init")
        
    def override(self):
        print ("CHILD override()")
```


```python
child = Child()
```

    Child init



```python
child.implicit()
```

    PARENT implicit()



```python
child.override()
```

    CHILD override()



```python
class Parent:
    def __init__(self):
        print("Parent init")
        
    def override(self, x=0):
        self.x = x
        print( "PARENT override()")

    def altered(self):
        print ("PARENT altered()", self.x)

class Child(Parent):
    def __init__(self):
        print("Child init")

    def altered(self):
        print ("CHILD, altered() Start")
        print(self.x)
        print ("CHILD, altered() End")
```


```python
c, d = Child(), Child()
```

    Child init
    Child init



```python
c.override(100)
```

    PARENT override()



```python
print(c.__dict__)
print(d.__dict__)
```

    {'x': 100}
    {}



```python
c.altered()
```

    CHILD, altered() Start
    100
    CHILD, altered() End



```python
try:
    d.altered()
except Exception as e:
    print(e)
```

    CHILD, altered() Start
    'Child' object has no attribute 'x'



```python
d.override(20)
try:
    d.altered()
    print(d.x, c.x)
except Exception as e:
    print(e)
```

    PARENT override()
    CHILD, altered() Start
    20
    CHILD, altered() End
    20 100



```python
# Another Bad example. 

class Parent:
    x = [10]   # Reason for it being a bad example.
    
    def update(self, val):
        self.x.append(val)
    
class Child(Parent):
    def altered(self):
        p = super(Child, self)
        print(type(p))
        print ("CHILD, BEFORE PARENT altered()")
        p.altered()
        print ("CHILD, AFTER PARENT altered()")
```


```python
# dad = Parent()
child1 = Child()
child2 = Child()

print(child1.x)
print(child2.x)
```

    [10]
    [10]



```python
child1.x.append(2000)
```


```python
print(child1.x)
print(child2.x)
```

    [10, 2000]
    [10, 2000]



```python
ch = Child("Mayank")
ch.username()
```

    Mayank



```python

```


```python
# # Bit better example but not good examples. 

class Parent:
    def __init__(self):
        self.x = [10]
    
    def update(self, val):
        self.x.append(val)
    
class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()

    def altered(self):
        print(type(self.p))
        print ("CHILD, BEFORE PARENT altered()")
#         self.p.altered()
        print ("CHILD, AFTER PARENT altered()")
```


```python
child1 = Child()
child2 = Child()

child1.update(100)
```


```python
print(child1.x)
print(child2.x)
```

    [10, 100]
    [10]



```python
# Problem of seperate init

class Parent:
    def __init__(self, title):
        self.title = tile
    
    def display(self, val):
        print(self.title, val)

class Child(Parent):
    def __init__(self, name):
        self.name = name
        
    def username(self):
        print(self.name)
```


```python
try:
    ch.display("Johri")
except Exception as e:
    print(e)
```

    'Child' object has no attribute 'title'



```python
# Problem of seperate init

class Parent:
    def __init__(self, title):
        self.title = title
    
    def display(self):
        print(self.title)

class Child(Parent):
    def __init__(self, name, title):
        self.name = name
        super(Child, self).__init__(title)
        
    def username(self):
        print(self.name)
        super(Child, self).display()
```


```python
# dad = Parent()
child1 = Child("Roshan", "MSI Interview Questions")
child2 = Child("Anuja", "AI and us")
```


```python
child1.display()
```

    MSI Interview Questions



```python
child2.username()
```

    Anuja
    AI and us



```python
child2.display()
```

    AI and us


#### Immutable data


```python
# Bit better example but not good examples. 

class Parent:
    x = 10
    def override(self):
        print( "PARENT override()")

    def altered(self):
        print ("PARENT altered()")
    
    def update(self, val):
        self.x = val
    
class Child(Parent):

    def override(self):
        print ("CHILD override()")

    def altered(self):
        p = super(Child, self)
        print(type(p))
        print ("CHILD, BEFORE PARENT altered()")
        p.altered()
        print ("CHILD, AFTER PARENT altered()")

dad = Parent()
child1 = Child()
child2 = Child()

child1.update(100)
print(child1.x)
print(child2.x)
```

    100
    10



```python
child2.altered()
```

    <class 'super'>
    CHILD, BEFORE PARENT altered()
    PARENT altered()
    CHILD, AFTER PARENT altered()



```python
class Parent:
    def __init__(self):
        self.x = 10
    
    def update(self, val):
        self.x = val
    
class Child(Parent):

    def altered(self, val):
        p = super(Child, self)
        p.update(val)

dad = Parent()
child1 = Child()
child2 = Child()

child1.altered(100)
print(child1.x)
print(child2.x)
```

    100
    10


## The Reason for `super()`

This should seem like common sense, but then we get into trouble with a thing called multiple inheritance. Multiple inheritance is when you define a class that inherits from one or more classes, like this:
```python
class SuperFun(Child, BadStuff):
    pass```

This is like saying, "Make a class named SuperFun that inherits from the classes Child and BadStuff at the same time."

In this case, whenever you have implicit actions on any SuperFun instance, Python has to look-up the possible function in the class hierarchy for both Child and BadStuff, but it needs to do this in a consistent order. To do this Python uses "method resolution order" (MRO) and an algorithm called C3 to get it straight.

Because the MRO is complex and a well-defined algorithm is used, Python can't leave it to you to get the MRO right. Instead, Python gives you the super() function, which handles all of this for you in the places that you need the altering type of actions as I did in Child.altered. With super() you don't have to worry about getting this right, and Python will find the right function for you.

### Using super() with __init__
The most common use of super() is actually in __init__ functions in base classes. This is usually the only place where you need to do some things in a child, then complete the initialization in the parent. Here's a quick example of doing that in the Child:

```python
class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()
```
This is pretty much the same as the Child.altered example above, except I'm setting some variables in the __init__ before having the Parent initialize with its Parent.__init__.


```python
class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()
```


```python
help(super)
```
