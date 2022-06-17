
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
- **Override Explicitly**: when you define a function in the parent, but not in the child. 


```python
class Parent():

    def override(self):
        print( "PARENT override()")

    def implicit(self):
        print ("PARENT implicit()")

    def altered(self):
        print ("PARENT altered()")

class Child(Parent):

    def override(self):
        print ("CHILD override()")

    def altered(self):
        p = super(Child, self)
        print ("CHILD, BEFORE PARENT altered()")
        p.altered()
        print ("CHILD, AFTER PARENT altered()")

dad = Parent()
child = Child()

dad.implicit()
child.implicit()

dad.override()
child.override()

dad.altered()
child.altered()
```

    PARENT implicit()
    PARENT implicit()
    PARENT override()
    CHILD override()
    PARENT altered()
    CHILD, BEFORE PARENT altered()
    PARENT altered()
    CHILD, AFTER PARENT altered()
    

## The Reason for super()

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
