
# Modules, Classes, and Objects & OOPS
----
Python is something called an “object- oriented programming language.” What this means is
there’s a construct in Python called a class that lets you structure your software in a particular
way. Using classes, you can add consistency to your programs so that they can be used in a cleaner
way, or at least that’s the theory.

Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class. An analogy is that you can have variables of type i n t which translates to saying that variables that store integers are variables which are instances (objects) of the int class.

Objects can store data using ordinary variables that belong to the object. Variables that
belong to an object or class are referred to as fields. Objects can also have functionality by
using functions that belong to a class. Such functions are called methods of the class. This
terminology is important because it helps us to differentiate between functions and
variables which are independent and those which belong to a class or object. Collectively,
the fields and methods can be referred to as the attributes of that class.

Fields are of two types - they can belong to each instance/object of the class or they can
belong to the class itself. They are called instance variables and class variables
respectively.

A class is created using the ***`class`*** keyword. The fields and methods of the class are listed
in an indented block.

## The self
Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name ***`self`***.

## Classes
---
A class is merely a container for static data members or function declarations, called a class's attributes. Classes provide something which can be considered a blueprint for creating "real" objects, called class instances. Functions which are part of classes are called ***`methods`***.

The simplest class possible is shown in the following example.
### Declare a Class
```python
class Class_name[( base_classes_if_any)]:
    "optional documentation string"
    static_member_declarations
    method_declarations
    ```


```python
# first.py

class First:
   pass

fr = First()
print (type(fr))
print (type(First))
```

    <class '__main__.First'>
    <class 'type'>
    


```python
# Example
class FooClass:
    """my very first class: FooClass"""
    __version = 0.11 # class (data) attribute
    ver = 0.1
    
    def __init__(self, nm='John Doe'):
        'constructor'
        self.name = nm # class instance (data) attribute
        print ('Created a class instance for: ', self.name)
    
    def showName(self):
        'display instance attribute and class name'
        print ('Your name is: ', self.name)
        print( 'My name is: ', self.__class__ )# full class name

    def showVersion(self):
        'display class(static) attribute'
        print( self.__version )# references FooClass.version
    
    def showVer(self):
        'display class(static) attribute'
        print( self.ver )# references FooClass.version 
    
    def setVersion(self, ver):
        'display class(static) attribute'
        self.__version = ver
        print( self.__version )# references FooClass.version  

# Create Class Instances
foo = FooClass()

# Calling class methods
foo.showName()
# print(foo.showName())
foo.showVer()
print(foo.ver)
foo.setVersion(10)
# print(foo.__version)
# print(FooClass.__version)
```

    Created a class instance for:  John Doe
    Your name is:  John Doe
    My name is:  <class '__main__.FooClass'>
    0.1
    0.1
    10
    


```python
class PrivateVariables():
    __version = 1.0
    _vers = 11.0
    ver = 10.0
    
    def show__version(self):
        print(self.__version)
    
    def show_vers(self):
        print(self._vers)

pv = PrivateVariables()
print(pv.ver)
print(pv._vers)
# print(pv.__version)

pv.ver = 111
print(pv.ver)
pv._vers = 1000
print(pv._vers) # Convension only 
```

    10.0
    11.0
    111
    1000
    

## attributes
In Python, attribute everything is contained inside an object. In Python there is no real distinction between plain data and functions, being both objects.

The following example represents a book with a title and an author. It also provides a `get_entry()` method which returns a string representation of the book.


```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_entry(self):
        return "{0} by {1}".format(self.title, self.author)
```

Every instance of this class will contain three attributes, namely `title, author`, and `get_entry`, in addition to the standard attributes provided by the object ancestor.


```python
b = Book(title="Akme", author="Mayank")
print(b.title)
b.title = "Akme Book"
print(b.title)
print(b.get_entry())
print(b.get_entry)
print(type(b.__dict__))
print(b.__dict__)
print(b.nonExistAttribute())
```

    Akme
    Akme Book
    Akme Book by Mayank
    <bound method Book.get_entry of <__main__.Book object at 0x000002A1F87BD978>>
    <class 'dict'>
    {'title': 'Akme Book', 'author': 'Mayank'}
    


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-22-a72461a43e6b> in <module>()
          7 print(type(b.__dict__))
          8 print(b.__dict__)
    ----> 9 print(b.nonExistAttribute())
    

    AttributeError: 'Book' object has no attribute 'nonExistAttribute'


Instead of using the normal statements to access attributes, you can use the following functions −

getattr
: to access the attribute of the object

The getattr(obj, name[, default]) 
: to access the attribute of object.
    
The hasattr(obj,name) 
: to check if an attribute exists or not.

The setattr(obj,name,value) 
    : to set an attribute. If attribute does not exist, then it would be created.

The delattr(obj, name)
    : to delete an attribute.

## Properties
Sometimes you want to have an attribute which value comes from other attributes or, in general, which value shall be computed at the moment. The standard way to deal with this situation is to create a method, called getter, just like I did with get_entry().

In Python you can "mask" the method, aliasing it with a data attribute, which in this case is called __***`property`***__.


```python
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_entry(self):
        return "{0} by {1}".format(self.title, self.author)

    entry = property(get_entry)

b = Book(title="Pawn of Prophecy", author="David Eddings")
print(b.entry)
```

    Pawn of Prophecy by David Eddings
    

Properties allow to specify also a write method (a setter), that is automatically called when you try to change the value of the property itself.


```python
class Book(object):
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def _get_entry(self):
        print("_get_entry")
        return "{0} by {1}".format(self.__title, self.__author)

    def _set_entry(self, value):
        if " by " not in value:
            raise ValueError("Entries shall be formatted as '<title> by <author>'")
        self.__title, self.__author = value.split(" by ")
    
    entry = property(_get_entry, _set_entry)

    def __getattr__(self, attr):
        print("Sorry attribure do not exist")
        return None


b = Book(title="Step in C", author="Mayank Johri")
print(b.entry)
b.entry = "Lets learn C by Mayank Johri"
print("*"*20)
print(b.entry)
print("*"*20)
b.entry = "Explore Go by Mayank Johri"
print("*"*20)
print(b.entry)
print(b.nonExistAttribute)
```

    _get_entry
    Step in C by Mayank Johri
    ********************
    _get_entry
    Lets learn C by Mayank Johri
    ********************
    ********************
    _get_entry
    Explore Go by Mayank Johri
    Sorry attribure do not exist
    None
    


```python

```
