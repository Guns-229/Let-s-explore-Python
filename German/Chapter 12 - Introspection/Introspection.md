
# Introspection

__Introspection__ or __reflection__ is the ability of software to identify and report their own internal structures, such as types, variable scope, methods and attributes.

Python provides multiple methods for introspection of the code. Few of them are listed below. 

| Function | Returns|
|----------|---------------------|
| `type(object)` |  The type/class of the object |
| `id(object)` |  object identifier |
| `locals()` |  dictionary containing local variables with values |
| `globals()` |  dictionary containing global variables with values  |
| `vars(object)` |  object symbols dictionary |
| `len(object)`  |  size of an object/collection |
| `dir(object)` |  A list of object attributes |
| `help(object)` |  Object's doc strings |
| `repr(object)` |  Object representation or `__repr__` function |
| `isinstance(object, class)` |  True if object is derived from class |
| `issubclass(subclass, class)` |  True if object inherits the class |

### `type`

It returns the type of the data being introspected as shown in the below example


```python
data_group = [
    1,    10.2,   3 + 4j,
    True, 0,      "ओ३म्",
    ["t", "l"]
]
for data in data_group:
    print(" {:20}: {}".format(str(data), type(data)))
```

     1                   : <class 'int'>
     10.2                : <class 'float'>
     (3+4j)              : <class 'complex'>
     True                : <class 'bool'>
     0                   : <class 'int'>
     ओ३म्                : <class 'str'>
     ['t', 'l']          : <class 'list'>


### `id(object)`

Return the “identity” of an object. This is an integer (or long integer) which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

> **NOTE**: CPython implementation detail: This is the address of the object in memory.


```python
a, b = 10, 20
print(a, id(a))
print(b, id(b))
```

    10 4491553872
    20 4491554192


### `vars(object)`

`vars` behave like `__dict__`, but with one exception, that it can be used to get other objects by passing them as parameters.


```python
class Apple(object):
    def __init__(self):
        self.a = "Apple"

a = Apple()

print(vars(a), a.__dict__)
a.color = "Green"
print(vars(a), a.__dict__)
```

    {'a': 'Apple'} {'a': 'Apple'}
    {'a': 'Apple', 'color': 'Green'} {'a': 'Apple', 'color': 'Green'}


#### `vars` acting as `locals`

When we don't provide any argument to `vars`, it acts as `locals` and returns local variables.


```python
class Apple(object):
    def __init__(self):
        self.a = "Apple"
        
    def intro(self):
        d = "Green Apple"
        return vars()
        
a = Apple()
print(a.intro())
```

    {'self': <__main__.Apple object at 0x10defa090>, 'd': 'Green Apple'}



```python
def intro(color):
    d = color
    return vars()
        
print(intro("Green"))
```

    {'color': 'Green', 'd': 'Green'}


The object identifier is a unique number that is used by the interpreter for identifying the objects internally.

    Example:


```python
# about global objects in the program

from types import ModuleType

def info(n_obj):

    # Create a referênce to the object
    obj = globals()[n_obj]

    # Show object information 
#     print('Name of object:', n_obj)
#     print('Identifier:', id(obj))
#     print('Typo:', type(obj))
    print('Representation:', repr(obj))

#     # If it is a module
#     if isinstance(obj, ModuleType):
#         print( 'itens:')
#         for item in dir(obj):
#             print (item)
    print

# # Showing information
for n_obj in dir()[:10]: # The slice [:10] is used just to limit objects
    info(n_obj)
```

    Representation: <class '__main__.Apple'>
    Representation: ['', 'data_group = [\n    1,    10.2,   3 + 4j,\n    True, 0,      "ओ३म्",\n    ["t", "l"]\n]\nfor data in data_group:\n    print(" {:20}: {}".format(str(data), type(data)))', 'a, b = 10, 20\nprint(a, id(a))\nprint(b, id(b))', 'class Apple(object):\n    def __init__(self):\n        self.a = "Apple"\n\na = Apple()\n\nprint(vars(a), a.__dict__)\na.color = "Green"\nprint(vars(a), a.__dict__)', 'class Apple(object):\n    def __init__(self):\n        self.a = "Apple"\n        \n    def intro(self):\n        d = "Green Apple"\n        return vars()\n        \na = Apple()\nprint(a.intro())', 'def intro(color):\n    d = color\n    return vars()\n        \nprint(intro("Green"))', "# about global objects in the program\n\nfrom types import ModuleType\n\ndef info(n_obj):\n\n    # Create a referênce to the object\n    obj = globals()[n_obj]\n\n    # Show object information \n#     print('Name of object:', n_obj)\n#     print('Identifier:', id(obj))\n#     print('Typo:', type(obj))\n    print('Representation:', repr(obj))\n\n#     # If it is a module\n#     if isinstance(obj, ModuleType):\n#         print( 'itens:')\n#         for item in dir(obj):\n#             print (item)\n    print\n\n# # Showing information\nfor n_obj in dir()[:10]: # The slice [:10] is used just to limit objects\n    info(n_obj)"]
    Representation: <class 'module'>
    Representation: {}
    Representation: ''
    Representation: ''
    Representation: ''
    Representation: <module 'builtins' (built-in)>
    Representation: <module 'builtins' (built-in)>
    Representation: 'Automatically created module for IPython interactive environment'


Python also has a module called *types*, which has the definitions of the basic types of the interpreter.

Example:


```python
import types

s = ' '
if isinstance(s, str):
    print('s is a string.')
```

    s is a string.


## `repr`


```python
class Users(object):
    def __init__(self, username, age):
        self.username = username
        self.age = age
        
chandu = Users("Chandu Nalluri", 45)
print(repr(chandu))
```

    <__main__.Users object at 0x10defed90>



```python
class Users(object):
    def __init__(self, username, age):
        self.username = username
        self.age = age
    
    def __repr__(self):
        return """This object contains following data
        name: {}, age: {}""".format(self.username, self.age)
        
chandu = Users("Chandu Nalluri", 45)
print(repr(chandu))
```

    This object contains following data
            name: Chandu Nalluri, age: 45


## `len`

`len` will return the number of elements present in the collection.


```python
# list
l = [1, 2, 3, 4, 5]
print(len(l))
```

    5



```python
# dictionary
l = {"test": "tes", "e": "d"}
print(len(l))
```

    2


Through introspection, it is possible to determine the fields of a database table, for example.

Inspect
-------
The module *inspect* provides a set of high-level functions that allow for introspection to investigate types, collection items, classes, functions, source code and the runtime stack of the interpreter.

Example:


```python
import os.path
# inspect: "friendly" introspection module
import inspect

print('Object:', inspect.getmodule(os.path))
print('Class?', inspect.isclass(str))
# Lists all functions that exist in "os.path"

print('Member:')

for name, struct in inspect.getmembers(os.path):

    if inspect.isfunction(struct):
        print(name, end=",") 
```

    Object: <module 'posixpath' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/posixpath.py'>
    Class? True
    Member:
    _get_sep,_joinrealpath,abspath,basename,commonpath,commonprefix,dirname,exists,expanduser,expandvars,getatime,getctime,getmtime,getsize,isabs,isdir,isfile,islink,ismount,join,lexists,normcase,normpath,realpath,relpath,samefile,sameopenfile,samestat,split,splitdrive,splitext,

The functions that work with the stack of the interpreter should be used with caution because it is possible to create cyclic references (a variable that points to the stack item that has the variable itself). The existence of references to stack items slows the destruction of the items by the garbage collector of the interpreter.


```python
import inspect


def myself():
    return inspect.stack()[1][3]

def parent_function():
    return inspect.stack()[2][3]


def power(expo):
    print("I am at {name}, {parent}".format(name=myself(), parent=parent_function()))
    def inner(num):
        print("I am at {name}, {parent}".format(name=myself(), parent=parent_function()))
        return num**expo
    return inner
              

def test_power(a, b):
    p = power(a)
    p(b)
```


```python
d = power(10)
d(10)
```

    I am at power, <module>
    I am at inner, <module>





    10000000000




```python
test_power(10, 5)
```

    I am at power, test_power
    I am at inner, test_power


## Reference

- http://stefaanlippens.net/python_inspect/
