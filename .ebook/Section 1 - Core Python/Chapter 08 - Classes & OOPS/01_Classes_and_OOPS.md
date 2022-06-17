
# Modules, Classes, and Objects & OOPS

Python is something called an “object- oriented programming language.” What this means is
there’s a construct in Python called a class that lets you structure your software in a particular
way. Using classes, you can add consistency to your programs so that they can be used in a cleaner
way, or at least that’s the theory.

Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class. An analogy is that you can have variables of type `int` which translates to saying that variables that store integers are variables which are instances (objects) of the int class.

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

## The `self`

Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name ***`self`***.

## Classes

A class is merely a container for static data members or function declarations, called a class's attributes. Classes provide something which can be considered a blueprint for creating "real" objects, called class instances. Functions which are part of classes are called ***`methods`***.

The simplest class possible is shown in the following example.


```python
# new Class
class Class_Name(object):
    pass

# old classes

class Class_Name_slow():
    pass

class Class_Name_for_lazy:
    pass
```

```python
class Class_Name(base_classes_if_any):
    """optional documentation string"""

    static_member_declarations = 1
    
    def method_declarations(self):
        """
        documentation
        """
        pass
```


```python
# first.py
class First(object):
    pass

fr = First()

print(type(fr), type(First))
print("~"*15)
print(type(10), int, type(int))
```

    <class '__main__.First'> <class 'type'>
    ~~~~~~~~~~~~~~~
    <class 'int'> <class 'int'> <class 'type'>



```python
# first.py
# Old class type
class First():
    pass

# So do not format `()` eles you are creating a variable
# Which is pointing to the Class and is not an object of that class

fr = First
print (type(fr), type(First))
print(fr is First)
```

    <class 'type'> <class 'type'>
    True



```python
# first.py

class User(object):
    def set_name(self, name):
        self.fullname = name

    def get_name(self):
        return self.fullname
```


```python
# Lets create an object of the class and find its attributes.
user = User()
print(dir(user))
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_name', 'set_name']



```python
# To find all the data variables (not attributes) exposed by the object.

print(user.__dict__)
```

    {}



```python
user.set_name("Manish Gupta")
print(dir(user))
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'fullname', 'get_name', 'set_name']



```python
print(user.get_name())
```

    Manish Gupta



```python
print(user.fullname)
```

    Manish Gupta



```python
# To find all the data variables (not attributes) exposed by the object.

print(user.__dict__)
```

    {'fullname': 'Manish Gupta'}



```python
# first.py

class User(object):
    def set_name(self, name):
        self.fullname = name

    def get_name(self):
        return self.fullname

user = User()
try:
    user.get_name()
except Exception as e:
    print("Error:", e)
```

    Error: 'User' object has no attribute 'fullname'



```python
# first.py
# Class with it's methods  
# wrong method to resolve the issue of attribute accessed before its created 
# use __getattr__ to resolve it as shown in the later examples.

class Second(object):
    def set_name(self, name):
        self.fullname = name
        
    def get_name(self):
        return self.fullname if "fullname" in self.__dict__ else None

try:
    sec = Second()
    print(sec.get_name())
except Exception as e:
    print("Error:", e)
```

    None



```python
# first.py
# Class with it's methods  
# wrong method to resolve the issue of attribute accessed before its created 
# use __getattr__ to resolve it as shown in the later examples.

class Second(object):
    def set_name(self, name):
        self.fullname = name
        
    def get_name(self):
        # One update, now using `get` function of dictionary to get the data
        return self.__dict__.get('fullname', None)

try:
    sec = Second()
    print(sec.get_name())
except Exception as e:
    print(e)
```

    None



```python
# To find all the variables exposed to the object.

print(sec.__dict__)
```

    {}


> <center><b>!!! NOTE !!!</b></center>
><hr>
> `self.x = y`. Assignation statements within the function will create the attribute if it does not exists.

#### `__init__` The Python Object Initializer


```python
# first.py

class User(object):
    def __init__(self, name):
        self.set_name(name)
        
    def set_name(self, name):
        self.fullname = name

    def get_name(self):
        return self.fullname
```


```python
# Lets create the object
user = User(name="Vishal Saxena")
print(dir(user))
print(user.get_name())
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'fullname', 'get_name', 'set_name']
    Vishal Saxena



```python
user = User("Vishal Saxena")
print(user.get_name())
```

    Vishal Saxena


> NOTE:
> <hr/>

> `self` is _NOT_ a **keyword**, but just a convension. Still for the sake of sanity for the developers to come, use `self` and not any other variable name. 


```python
### Just for fun
# स्वयं is myself in Hindi

class FunClass(object):
    def __init__(स्वयं, name):
        स्वयं.name = name

fc = FunClass("Mayank")
print(fc.name)
```

    Mayank



```python
# __init__ supports default arguments also.

class User(object):
    def __init__(self, name, age=35):
        self.name(name)
        self.age = age
        
    def name(self, new_name):
        self.fullname = new_name
        
    def get_name(self):
        return self.fullname
```


```python
# First Object
arya = User(name="Arya")
print(arya.get_name(), "is", arya.age, "years old")
```

    Arya is 35 years old



```python
# Second Object

rajni = User("Rajneekanth", 20)
print(rajni.get_name(), "is", rajni.age, "years old")
```

    Rajneekanth is 20 years old



```python
# Two objects of the same class need not be same
arya == rajni
```




    False




```python
arya2 = User("Arya")
```


```python
# Although both arya and arya2 have same data 
# But they will by default fail in `==` comparision.
# Please implement __eq__(self) attribure in your class
arya == arya2
```




    False




```python
print(id(arya), id(arya2))
```

    4587554832 4587395216



```python
# first.py

class User(object):
    fullname = "Mayank Johri"
    age = 43
        
    def name(self, name):
        self.fullname = name
        
    def get_name(self):
        return self.fullname
```


```python
rahul = User()
print(rahul.get_name(), "is", rahul.age, "years old")
rajni = User()
print(rajni.get_name(), "is", rajni.age, "years old")
```

    Mayank Johri is 43 years old
    Mayank Johri is 43 years old



```python
print(rahul.fullname, id(rahul.fullname))
print(rajni.fullname, id(rajni.fullname))
```

    Mayank Johri 4587746864
    Mayank Johri 4587746864



```python
rahul.name("Rahul Johri")
```


```python
print(rahul.fullname, id(rahul.fullname))
print(rajni.fullname, id(rajni.fullname))
```

    Rahul Johri 4587759344
    Mayank Johri 4587746864



```python
# first.py

class Bridge(object):
    fullname = "Ram Setu"
    age = 33
    __CONST = "India"
        
    def name(self, name):
        self.fullname = name
        
    def get_name(self):
        return self.fullname, self.__CONST
```


```python
rs_1 = Bridge()
rs_2 = Bridge()
```


```python
print(rs_1.fullname == rs_2.fullname)
print(id(rs_1.fullname) == id(rs_2.fullname))
```

    True
    True



```python
# Still object are not same. :(
print(rs_1 == rs_2)
```

    False



```python
print(rs_1.get_name())
```

    ('Ram Setu', 'India')



```python
rs_1.name("ram setu")
```


```python
print(rs_1.fullname == rs_2.fullname)
print(id(rs_1.fullname) == id(rs_2.fullname))
```

    False
    False



```python
print(rs_1.fullname, " - ", rs_2.fullname)
```

    ram setu  -  Ram Setu


- The magic of `mutables`


```python
class Users(object):
    user_list = ["Mayank", "Aalok"]
    age = 33
        
    def name(self, name):
        self.user_list.append(name)
        
    def get_name(self):
        return self.user_list
```


```python
rs_1 = Users()
rs_2 = Users()
```


```python
print(rs_1.user_list, rs_2.user_list)
```

    ['Mayank', 'Aalok'] ['Mayank', 'Aalok']



```python
print(rs_1.user_list is rs_2.user_list)
print(id(rs_1.user_list) == id(rs_2.user_list))
```

    True
    True



```python
rs_1.name("A-Shanti")
```


```python
# Values in both the object got updated. 
print(rs_1.user_list, rs_2.user_list)
```

    ['Mayank', 'Aalok', 'A-Shanti'] ['Mayank', 'Aalok', 'A-Shanti']



```python
print(rs_1.user_list is rs_2.user_list)
print(id(rs_1.user_list) == id(rs_2.user_list))
```

    True
    True



```python
# For Cases where you need to have some data at class level and some at object level. 
# For object level populate them in __init__ function

class UserDetails:
    users_list = ["Mayank", "Johri"]
    
    def __init__(self, name, age = 2400):
        self.name(name)
        self.age = age # The Man from Earth Guy. 
        
    def name(self, name):
        self.users_list.append(name)
        
    def get_name(self):
        return self.users_list
```


```python
rs_1 = UserDetails("Ram Setu")
rs_2 = UserDetails("London Bridge", 120)
```


```python
print(rs_1.users_list == rs_2.users_list)
print(id(rs_1.users_list) == id(rs_2.users_list))
```

    True
    True



```python
print(rs_1.users_list, " - ", rs_2.users_list)
```

    ['Mayank', 'Johri', 'Ram Setu', 'London Bridge']  -  ['Mayank', 'Johri', 'Ram Setu', 'London Bridge']



```python
print(id(rs_1.age), rs_1.age)
print(id(rs_2.age), rs_2.age)
```

    4561172720 2400
    4523977232 120


In the below example, attributes are no longer sharing the same memory space and will not be created at the time of object creation but will be created at the time of object initialization


```python
class Bridge:
    def __init__(self, name):
        self.fullname = ["Mayank", "Johri"]
        self.name(name)
        self.age = 33
        
    def name(self, name):
        self.fullname.append(name)
        
    def get_name(self):
        return self.fullname
```


```python
rs_1 = Bridge("Ram Setu")
rs_2 = Bridge("London Bridge")
```


```python
print(rs_1.fullname, " : ", rs_2.fullname)
print(rs_1.fullname == rs_2.fullname)
print(id(rs_1.fullname) == id(rs_2.fullname))
```

    ['Mayank', 'Johri', 'Ram Setu']  :  ['Mayank', 'Johri', 'London Bridge']
    False
    False



```python
print(rs_1.fullname == rs_2.fullname)
print(id(rs_1.fullname) == id(rs_2.fullname))
```

    False
    False



```python
print(rs_1.fullname, " - ", rs_2.fullname)
```

    ['Mayank', 'Johri', 'Ram Setu']  -  ['Mayank', 'Johri', 'London Bridge']



```python
class HardDisks(object):
    __version = "0.0.1"
    _build_ver = "1.0.1"
    type = "HDD"
    
    def __init__(self, size, brand):
        self.size = size
        self.brand = brand
        
    def get_size(self):
        return self.size
    
    def set_size(self, size):
        self.size = size
```


```python
hd = HardDisks(100, "Sony")
```


```python
hd.get_size()
```




    100




```python
print(dir(hd))
```

    ['_HardDisks__version', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_build_ver', 'brand', 'get_size', 'set_size', 'size', 'type']



```python
print(hd.__dict__)
```

    {'size': 100, 'brand': 'Sony'}



```python
class HardDisks(object):
    
    def __init__(self, size, brand):
        self.size = size
        self.brand = brand
        self.__version = "0.0.1"
        self._build_ver = "1.0.1"
        self.type = "HDD"
        
    def get_version(self):
        return self.__version
    
    def set_version(self, version):
        self.__version = version
```


```python
hd = HardDisks(100, "Sony")
print(hd.get_version())
print(dir(hd))
print(hd.__dict__)
```

    0.0.1
    ['_HardDisks__version', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_build_ver', 'brand', 'get_version', 'set_version', 'size', 'type']
    {'size': 100, 'brand': 'Sony', '_HardDisks__version': '0.0.1', '_build_ver': '1.0.1', 'type': 'HDD'}



```python
try:
    print(hd.__version)
except Exception as e:
    print(e)
```

    'HardDisks' object has no attribute '__version'



```python
try:
    print(hd._build_ver)
except Exception as e:
    print(e)
```

    1.0.1


### Updating class attribute containing immutable data type


```python
class Foo(object):
    ver = 20
    def setVersion(self, val):
        pass
    
    def showVer(self):
        return self.ver

foo = Foo()
foo.setVersion(10)  # __version
foo.ver = 2020202   # ver
```


```python
foo.showVer()
```




    2020202



### Updating class attribute contains mutable data type


```python
foo._vers.append(0.011)
```


```python
print(foo._vers, id(foo._vers))
print(arya._vers, id(arya._vers))
```

    ['0.0.1', '0.0.2', '0.0.3', '0.11', 0.011] 84986312
    ['0.0.1', '0.0.2', '0.0.3', '0.11', 0.011] 84986312


### Object Attributes

They are not shared across the class, but are different for different object of the same class.


```python
print(foo.name)
```

    John Doe



```python
foo.name = "Anamika Johri"
print(foo.name)
print(arya.name)
```

    Anamika Johri
    Arya



```python
foo.showVer()
print(foo.ver)
print("-"*20)
print(arya.showVer())
```

    0.1
    0.1
    --------------------
    0.1
    None



```python
try:
    print(foo.__version)
except Exception as e:
    print(e)
```

    'FooClass' object has no attribute '__version'



```python
try:
    print(foo.__getattribute__("__version"))
except Exception as e:
    print(e)
```

    'FooClass' object has no attribute '__version'



```python
# Example
class User(object):
    """my very first class: FooClass"""
    
    def __init__(self, firstname='John', surname="Doe"):
        'constructor'
        self.name = firstname + " " + surname 
        print ('Created a class instance for: ', self.name)
    
    def showName(self):
        'display instance attribute and class name'
        print ('Your name is: ', self.name)
        print( 'My name is: ', self.__class__ )  # full class name

# Create Class Instances
user = User()
arya = User("Arya")
gupta = User(surname="Gupta")
```

    Created a class instance for:  John Doe
    Created a class instance for:  Arya Doe
    Created a class instance for:  John Gupta



```python
user.showName()
arya.showName()
gupta.showName()
```

    Your name is:  John Doe
    My name is:  <class '__main__.User'>
    Your name is:  Arya Doe
    My name is:  <class '__main__.User'>
    Your name is:  John Gupta
    My name is:  <class '__main__.User'>



```python
# Example
class User(object):
    """my very first class: FooClass"""
    
    def __init__(self, firstname, surname):
        'initializer is not a constructor'
        self.name = firstname + " " + surname 
        print ('Created a class instance for: ', self.name)
    
    # full class name
    def showName(self):
        'display instance attribute and class name'
        print ('Your name is: ', self.name)
        print( 'My name is: ', self.__class__ )
```


```python
# Create Class Instances
try:
    user = User()
#     arya = User("Arya")
#     gupta = User(surname="Gupta")
#     gupta = User(surname="Gupta", firstname="Manish")
    arya.showName()
except Exception as e:
    print(e)
```

    __init__() missing 2 required positional arguments: 'firstname' and 'surname'


So, we can't have any object creation with lesser than two parameters. Lets comment out the first three object creation code and try again


```python
# Create Class Instances
try:
#     user = User()
#     arya = User("Arya")
#     gupta = User(surname="Gupta")
    gupta = User(surname="Gupta", firstname="Manish")
    arya.showName()
except Exception as e:
    print(e)
```

    Created a class instance for:  Manish Gupta
    Your name is:  Arya Doe
    My name is:  <class '__main__.User'>


### Attributes Type, private & public


```python
class PrivateVariables(object):
    def __init__(self):
        self.__version = 1.0
        self._vers = 11.0
        self.ver = 10.0
    
    def show_version(self):
        return(self.__version)
    
    def update_version(self, ver):
        self.__version = ver
    
    def show_vers(self):
        print(self._vers)
    
    def __private_funct(self):
        pass
```


```python
pv = PrivateVariables()
```


```python
print(dir(pv))
```

    ['_PrivateVariables__private_funct', '_PrivateVariables__version', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_vers', 'show_vers', 'show_version', 'update_version', 'ver']



```python
# Using Hack to call private variable:
print(pv._PrivateVariables__version)
```

    1.0



```python
print(pv.ver)
print(pv._vers)

try:
    print(pv.__version)
except Exception as e:
    print(e)
```

    10.0
    11.0
    'PrivateVariables' object has no attribute '__version'



```python
pv.ver = 111
print(pv.ver)
pv._vers = 1000  # Convension only not to update outside the class/object
print(pv._vers)   
print(pv.show_version())
```

    111
    1000
    1.0



```python
print(pv.__dict__)
```

    {'ver': 111, '_vers': 1000}


#### Private Methods

To create a private method, the function name should start with double underscore, but **not end** with double underscore.


```python
class PrivateAttributes(object):
    def __hidden(self, val):
        return val * 2

    def show(self, val):
        return self.__hidden(val)        
```


```python
pa = PrivateAttributes()
```


```python
print(pa.__dict__)
print(pa.__dir__())
```

    {}
    ['__module__', '_PrivateAttributes__hidden', 'show', '__dict__', '__weakref__', '__doc__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']


### Investigating the attributes existance

Say we are trying to find if `__vesion` is an attribute of the object `pv`


```python
print(pv.__dict__.get('__version', "None"))
```

    None



```python
print(pv.__dict__.get('ver', 'None'))
```

    None


To check if attribute exists in an object we can use `in` as in the above example, the attribute might contain the default values, thus rendering our solution ineffective.


```python
'__version' in pv.__dict__ 
```




    False




```python
'ver' in pv.__dict__ 
```




    True



### Adding/Update new object attribute


```python
# Not a recommended way.

pv.__dict__['new_ver'] = 1010
print(pv.__dict__.get('new_ver'))
```

    1010



```python
pv.new_ver
```




    1010




```python
print(dir(pv))
```

    ['_PrivateVariables__private_funct', '_PrivateVariables__version', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_vers', 'new_ver', 'show_vers', 'show_version', 'update_version', 'ver']



```python
# This is the better method

pv.test = "TESting"
```


```python
print(dir(pv))
```

    ['_PrivateVariables__private_funct', '_PrivateVariables__version', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_vers', 'new_ver', 'show_vers', 'show_version', 'test', 'update_version', 'ver']



```python
print(dir(pv))
```

    ['_PrivateVariables__version', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_vers', 'show_vers', 'show_version', 'update_version', 'ver']



```python
try:
    print(pv.__version)
except Exception as e:
    print(e)
```

    'PrivateVariables' object has no attribute '__version'



```python
# monkey patching
def sum(a, b):
    return a + b

pv.sum = sum 
print(pv.sum(10, 20))
```

    30


### `static` / `class` variables 

**Reference:** 
[https://stackoverflow.com/questions/68645/are-static-class-variables-possible](https://stackoverflow.com/questions/68645/are-static-class-variables-possible).

`Static variables` are variables **declared inside the class definition**, and not inside a _method_ are **class** or **static** variables.

But before you go all, _Yahooooo..._ about understanding of `static variables`. Please note that the implementation of static variables in python are different from Java/C++, they are unique in many ways. 

Lets understand them a little using the following code


```python
class Static_Test(object):
    val = "Rajeev Chaturvedi"
```


```python
s = Static_Test()
```


```python
print(s.val,"\b,", id(s.val))
print(Static_Test.val, "\b,", id(Static_Test.val))
```

    Rajeev Chaturvedi , 87826056
    Rajeev Chaturvedi , 87826056


So far so good, val & id of val from both the `instance` and `class` _seems_ to be same, thus they are pointing to same memory location which contains the value.
Now lets try to update it in class


```python
Static_Test.val = "राजीव चतुर्वेदी"
```


```python
print(s.val,"\b,", id(s.val))
print(Static_Test.val, "\b,", id(Static_Test.val))
s_new = Static_Test()
print(s_new.val,"\b,", id(s.val))
```

    राजीव चतुर्वेदी , 91993360
    राजीव चतुर्वेदी , 91993360
    राजीव चतुर्वेदी , 91993360


So, if we update values at class level, than they are getting reflected in all the instances as well. Now lets try to update its value in an instance and check its effect


```python
s.val = "Sachin"
print(s.val,"\b,", id(s.val))
print(Static_Test.val, "\b,", id(Static_Test.val))
s_new = Static_Test()
print(s_new.val,"\b,", id(s.val))
```

    Sachin , 140463287695320
    राजीव चतुर्वेदी , 140463287335304
    राजीव चतुर्वेदी , 140463287695320


Once, instance value has been changed then it remain changed and cannot be reverted by changing `class` variable value as shown in the below code


```python
Static_Test.val = "Sachin Shah"
print(s.val,"\b,", id(s.val))
print(Static_Test.val, "\b,", id(Static_Test.val))
s_new = Static_Test()
print(s_new.val,"\b,", id(s.val))
```

    Sachin , 140463287695320
    Sachin Shah , 140463287378800
    Sachin Shah , 140463287695320


### Static and Class Methods

Python provides decorators `@classmethod` & `@staticmethod` 

#### `@staticmethod`

A `static` method does not receive an implicit first argument (`self` or `cls`). To declare a `static` method decorator `staticmethod` is used as shown in the below example


```python
class Circle(object):
    PI = 3.14
    
    @staticmethod
    def area_circle(radius):
        area = 0
        try:
            area = PI * radius * radius
        except Exception as e:
            print(e)
        return area

c = Circle()
print(c.area_circle(10))
```

    name 'PI' is not defined
    0


As shown in the above example, static methods do not have access to any class or instance attributes. We tried to access class attribute `PI` and received error message that variable not defined.

Static methods for all intent and purpose act as normal function, but are called from within an `object` or `class`.

Static methods similar to class methods are bound to a `class` instead of its object, thus do not require a class instance creation and thus are not dependent on the state of the object.

Still there are few noticible differences between a static method and a class method, few of them are as follows:

- Static method are isolated from its class/object and have access only to the parameters passed to it.
- Class method works with the class since its parameter is always the class itself.

#### When do you use static method

So, if they do not have access to the class, then why are they created. We will try to understand the logic of why they should be created.

#####  Grouping utility function to a class

Many times, we have to few function, which are used by an object but are not part of the object and are not used by any other object. 


```python
class User(object):
    def __init__(self, name, age, height, weight, waist_size):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.waist_size = waist_size
    
    def get_details(self, func):
        funcs = {
            'bmi': [self._bmi_calculate, self.height, self.weight],
            'fat_mass': [self._fat_mass, self.weight, self.waist_size]
        }
        return funcs[func][0](*funcs[func][1:])
        
    @staticmethod
    def _bmi_calculate(height, weight):
        print(height, weight)
        return round(weight / (height * height), 2)
        
    @staticmethod
    def _body_fat_estimator(weight, waist_size):
        # (-76.76 + (4.15 * Waist) - (.082 * Weight)) / Weight
        pass
    
    @staticmethod
    def _fat_mass(weight, waist_size):
        # Body Fat % * Weight
        pass
    
    @staticmethod
    def _lean_mass(weight, waist_size):
        # Weight - Fat Mass
        pass
    

mayank = User("Mayank", 43, 1.89 , 72, 44)

print(mayank.get_details('bmi'))
```

    1.89 72
    20.16


#### Isolating object data from functions.

Although static methods, allows to hide non necessary class/object data from the function as shown in the below example.  


```python
class User(object):
    def __init__(self, marks, name):
        self.marks = marks
        self.name = name
    
    @staticmethod
    def banner(name):
        name = f"{name:^60}"
        print("~^"*30)
        print(name)
        print("~^"*30)
        
    
marks = [81, 85, 72, 92]

user = User(marks, "Rakesh Saxena")
user.banner(user.name)
print(user.name)
```

    ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^
                           Rakesh Saxena                        
    ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^
    Rakesh Saxena


But, they can not protect if `mutable` data is passed and updated inside the static function as shown in the below example. 


```python
class User(object):
    def __init__(self, marks, name):
        self.marks = marks
    
    @staticmethod
    def average(marks):
        marks.append(100)
        return sum(marks)/len(marks)
    
marks = [81, 85, 72, 92]

user = User(marks, "Rakesh Saxena")
user.average(user.marks)
print(user.marks)
```

    [81, 85, 72, 92, 100]


In the above example, mutable data `user.marks` was passed, and we were able to update them within the `staticmathod` `average`.  

## Magic Methods

### `__str__`

The method should be implemented when we wish to provide details 

### `__repr__`


```python

```


```python

```

### `__str__` vs `__repr__`


```python

```

### `__class__`


```python

```

### `__name__`


```python

```

### `__getattribute__`


```python

```

### `__dict__`


```python

```

### `__call__`


```python

```

## attributes
In Python, attribute is everything, contained inside an object. In Python there is no real distinction between plain data and functions, being both objects.

The following example represents a book with a title and an author. It also provides a `get_entry()` method which returns a string representation of the book.


```python
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_entry(self):
        return f"{self.title} by {self.author}"
```

Every instance of this class will contain three attributes, namely `title, author`, and `get_entry`, in addition to the standard attributes provided by the object ancestor.


```python
b = Book(title="Akme", author="Mayank")
```


```python
print(dir(b))
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'author', 'get_entry', 'title']



```python
print(b.title)
b.title = "Lets Go"

print(b.title)
print(b.get_entry())
```

    Akme
    Lets Go
    Lets Go by Mayank


Instead of using the normal statements to access attributes, you can also use the following functions −

`getattr`
: to access the attribute of the object

The `getattr(obj, name[, default]) `
: to access the attribute of object.
    
The `hasattr(obj, name) `
: to check if an attribute exists or not.

The `setattr(obj, name, value) `
    : to set an attribute. If attribute does not exist, then it would be created.

The `delattr(obj, name)`
    : to delete an attribute.


```python
class Book_Old(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
```


```python
b1 = Book_Old("Lets Explore C", "Mayank Johri")
print(b1.title, b1.author)
```

    Lets Explore C Mayank Johri



```python
print(getattr(b1, 'title'))
print(getattr(b1, 'title1', "None"))
```

    Lets Explore C
    None



```python
print(hasattr(b1, 'title'))
print(hasattr(b1, 'title_1'))
```

    True
    False



```python
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_entry(self):
        return f"{self.title} by {self.author}"
    
    def set_entry(self, val):
        self.title, self.author = val.split(" by ")
```


```python
b = Book(title="Akme", author="Mayank")
print(b.__dict__)
```

    {'title': 'Akme', 'author': 'Mayank'}



```python
b.set_entry("Lets Explore python by Mayank Johri")
print(b.__dict__)
```

    {'title': 'Lets Explore python', 'author': 'Mayank Johri'}


## Properties
Sometimes you want to have an attribute whose value comes from other attributes or, in general, which value shall be computed at the moment. The standard way to deal with this situation is to create a method, called getter, just like I did with get_entry().

In Python you can "mask" the method, aliasing it with a data attribute, which in this case is called __***`property`***__.


```python
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __get_entry(self):
        return "{title} by {author}".format(title=self.title, 
                                            author=self.author)

    entry = property(__get_entry)

b = Book(title="Lets Explore Advance Python", author="Mayank Johri")
print(b.entry)
```

    Lets Explore Advance Python by Mayank Johri


Properties allow to specify also a write method (a setter), that is automatically called when you try to change the value of the property itself.

> NOTE: 

>    Don't Worry to much about properties, we have entire chapter dedicated for it. 


```python
class User(object):
    def __init__(self, name):
        self.__name = name
    
    def __get_name(self):
        return "User's full name is: {0}".format(self.__name) 
    
    def __set_name(self, name):
        self.__name = name

    fullname = property(__get_name, __set_name)
```


```python
user = User("Roshan Musheer")
```


```python
print(user.__dict__)
```

    {'_User__name': 'Roshan Musheer'}



```python
print(user.fullname)
```

    User's full name is: Roshan Musheer



```python
## Setting the value of property

user.fullname = "Shaeel Parez"
print(user.fullname)
```

    User's full name is: Shaeel Parez



```python
## fully python guys
## '_User__name', '_User__getname', '_User__setname'
# Cheating to get the value

print(user._User__name)
```

    Shaeel Parez



```python
## Only setter property
## Something not right.
class TestSetter():
    def setter(self, name):
        self.name = name
    myname = property(fset=setter)
    
ts = TestSetter()

ts.myname = "Mayank"
print(ts.name)
```

    Mayank



```python
### !!! Gotcha !!!
try:
    print(ts.myname)
except Exception as e:
    print(e)
```

    unreadable attribute



```python
## Only getter property

class A:
    def get_x(self, neg=False):
        return -5 if neg else 5
    x = property(get_x)
    
a = A()
print(a.x)
```

    5



```python
class Book(object):
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def __get_entry(self):
        return "{0} by {1}".format(self.__title, self.__author)

    def __set_entry(self, value):
        if " by " not in value:
            raise ValueError("Entries shall be formatted as '<title> by <author>'")
        self.__title, self.__author = value.split(" by ")
    
    entry = property(__get_entry, __set_entry)

    def __getattr__(self, attr):
        """
        This function gets called when requested attribute do not exist
        """
        print("Sorry attribure do not exist:", attr)
        return None
```


```python
b = Book(title="Step in C", author="Mayank Johri")
print(b.entry)
```

    Step in C by Mayank Johri



```python
b.entry = "Lets learn C by Mayank Johri"
print(b.entry)
```

    Lets learn C by Mayank Johri



```python
b.entry = "Explore Go by Mayank Johri"
print(b.entry)
```

    Explore Go by Mayank Johri



```python
print(b.__dict__)
```

    {'_Book__title': 'Explore Go', '_Book__author': 'Mayank Johri'}


#### Handling non existing attributes


```python
# due to __getattr__

b.nonExistAttribute37
```

    Sorry attribure do not exist: nonExistAttribute


## The constructor `__new__` 

`__new__` is called for new Class type, 

### Overriding the __new__ method

As per "https://www.python.org/download/releases/2.2/descrintro/#__new__"

Here are some rules for `__new__`:

- `__new__` is a static method. When defining it, you don't need to (but may!) use the phrase "`__new__` = staticmethod(`__new__`)", because this is implied by its name (it is special-cased by the class constructor).
- **The first argument to `__new__` must be a class**; the remaining arguments are the arguments as seen by the constructor call.
- A `__new__` method that overrides a base class's `__new__` method may call that base class's `__new__` method. The first argument to the base class's `__new__` method call should be the class argument to the overriding `__new__` method, not the base class; if you were to pass in the base class, you would get an instance of the base class.
- Unless you want to play games like those described in the next two bullets, a `__new__` method must call its base class's `__new__` method; that's the only way to create an instance of your object. The subclass `__new__` can do two things to affect the resulting object: pass different arguments to the base class `__new__`, and modify the resulting object after it's been created (for example to initialize essential instance variables).
- `__new__` must return an object. There's nothing that requires that it return a new object that is an instance of its class argument, although that is the convention. If you return an existing object, the constructor call will still call its `__init__` method. If you return an object of a different class, its `__init__` method will be called. If you forget to return something, Python will unhelpfully return None, and your caller will probably be very confused.
- For immutable classes, your `__new__` may return a cached reference to an existing object with the same value; this is what the int, str and tuple types do for small values. This is one of the reasons why their `__init__` does nothing: cached objects would be re-initialized over and over. (The other reason is that there's nothing left for `__init__` to initialize: `__new__` returns a fully initialized object.)
- If you subclass a built-in immutable type and want to add some mutable state (maybe you add a default conversion to a string type), it's best to initialize the mutable state in the `__init__` method and leave `__new__` alone.
- If you want to change the constructor's signature, you often have to override both `__new__` and `__init__` to accept the new signature. However, most built-in types ignore the arguments to the method they don't use; in particular, the immutable types (int, long, float, complex, str, unicode, and tuple) have a dummy `__init__`, while the mutable types (dict, list, file, and also super, classmethod, staticmethod, and property) have a dummy `__new__`. The built-in type 'object' has a dummy `__new__` and a dummy `__init__` (which the others inherit). The built-in type 'type' is special in many respects; see the section on metaclasses.
- (This has nothing to do to `__new__`, but is handy to know anyway.) If you subclass a built-in type, extra space is automatically added to the instances to accomodate __dict__ and __weakrefs__. (The __dict__ is not initialized until you use it though, so you shouldn't worry about the space occupied by an empty dictionary for each instance you create.) If you don't need this extra space, you can add the phrase "``__slots__` = []`" to your class. (See above for more about `__slots__`.)
- Factoid: `__new__` is a static method, not a class method. I initially thought it would have to be a class method, and that's why I added the classmethod primitive. Unfortunately, with class methods, upcalls don't work right in this case, so I had to make it a static method with an explicit class as its first argument. Ironically, there are now no known uses for class methods in the Python distribution (other than in the test suite). I might even get rid of classmethod in a future release if no good use for it can be found!


### What is the difference between `__new__` and `__init__`

Use `__new__` when you need to control the creation of a new instance. Use `__init__` when you need to control initialization of a new instance.

`__new__` is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class. In contrast, `__init__` doesn't return anything; it's only responsible for initializing the instance after it's been created.

In general, you shouldn't need to override `__new__` unless you're subclassing an immutable type like str, int, unicode or tuple.

From: http://mail.python.org/pipermail/tutor/2008-April/061426.html


```python
# Very very very bad example, do not use it in production ever 
# except when you really want that only. 

class MyTest(object):
    def __new__(cls):
        print("in new")
        
    def __init__(self):
        print("in init")
```

    in new



```python
# Why not to mess with __new__
mnt = MyTest()
print(type(mnt))
```

    in new
    <class 'NoneType'>


Since the object was never created `__init__` function was never called. 


```python
# We can have multiple constructors 
# AGain BAD BAD code, do not use in production.

class MyNewTest:
    def __new__(self, name):
        print("in new with argument", name)
        
    def __init__(self, name):
        print("in init", name)

mnt = MyNewTest("Hari Hari")
```

    in new with argument Hari Hari


Lets look at another example, we have removed the `__new__` method from the above class and created an object. As `__new__` is not returning anything the object was never created.


```python
class MyNewTest:        
    def __init__(self, name):
        print("in init", name)

mnt = MyNewTest("Hari Hari")
```

    in init Hari Hari



```python
print(type(mnt))
```

    <class '__main__.MyNewTest'>


In the above example, we let Python create the object for us and just used the initializer to update the object.

Now lets check where its goog idea to use `__init__` and where `__new__`. 

One thumb rule is try to avoid using `__new__` and let python handle it because almost all the things you wish to do in constructor can be done in `__init__`. Still if you wish to do so, below examples will show you how to do it currectly.

In the first example, we have `__init__` function and are using it. 


```python
class MyNewTest:        
    def __init__(self, name):
        print("in init", name)
        self.name = name
        
    def print_name(self):
        print(self.name)


mnt = MyNewTest("Hari Hari")
mnt.print_name()
```

    in init Hari Hari
    Hari Hari


We saw, that everything was working without any issue. Now lets try to replace `__init__` with `__new__`. 


```python
# -----------------#
# Very Bad Example #
# -----------------#
class MyNewTest:        
    def __new__(cls, name):
        print("in init", name)
        cls.name = name
        
    def print_name(self):
        print(self.name)

try:
    mnt = MyNewTest("Hari Hari")
    mnt.print_name()
except Exception as e:
    print(e)
```

    in init Hari Hari
    'NoneType' object has no attribute 'print_name'


Now, since we have not returned any thing in `__new__` thus `mnt` is null. We must have `__new__` which returns the object itself. Now to over come this issue, we need to return an instance of our `class`. We can do that using `instance = super(<class>, cls).__new__(cls)` as shown in the below example 


```python
# First proper constructor

class MyNewTest(object):        
    def __new__(cls, name):
        print("in __new__:\n\t{0}".format(name))
        instance = super(MyNewTest, cls).__new__(cls)
        instance.name = name
        return instance

    def print_name(self):
        print("print_name:\n\t{0}".format(self.name))
        
hari = MyNewTest("!!! Hari Om Hari Om !!!")
hari.print_name()

ram_ram = MyNewTest("!!! Ram Ram !!!")
ram_ram.print_name()
hari.print_name()
```

    in __new__:
    	!!! Hari Om Hari Om !!!
    print_name:
    	!!! Hari Om Hari Om !!!
    in __new__:
    	!!! Ram Ram !!!
    print_name:
    	!!! Ram Ram !!!
    print_name:
    	!!! Hari Om Hari Om !!!


or, we can create the class using the following code, `instance =  object.__new__(cls)`. As object is parent, we are directly calling it instead of using `super`.


```python
class MyNewTest(object):        
    def __new__(cls, name):
        print("in __new__", name)
        instance =  object.__new__(cls)
        instance.name = name
        print("exiting __new__", name)
        return instance
    
    # __init__ is redundent in this example. 
    def __init__(self, name): 
        print("in __init__", name)
        # self.name = name
    
    def print_name(self):
        print(self.name)
```


```python
mnt = MyNewTest("Hari Hari")
```

    in __new__ Hari Hari
    exiting __new__ Hari Hari
    in __init__ Hari Hari



```python
mnt.print_name()
```

    Hari Hari



```python
ram_ram = MyNewTest("Ram Ram")
print(ram_ram)
```

    in __new__ Ram Ram
    exiting __new__ Ram Ram
    in __init__ Ram Ram
    <__main__.MyNewTest object at 0x0000000005640908>


both `super(MyNewTest, cls).__new__(cls)` and `object.__new__(cls)` produce the desired instance as shown in the above examples.


```python
## First proper constructor and initializer example. 

class MyNewTest(object):        
    def __new__(cls, name):
        print("in __new__", name)
        instance =  object.__new__(cls)
        print("exiting __new__", name)
        return instance
    
    def __init__(self, name):    
        print("in __init__", name)
        self.name = name
    
    def print_name(self):
        print(self.name)
        
hari = MyNewTest("Hari Hari")
ram_ram = MyNewTest("Ram Ram")
hari.print_name()
print(ram_ram.name)
```

    in __new__ Hari Hari
    exiting __new__ Hari Hari
    in __init__ Hari Hari
    in __new__ Ram Ram
    exiting __new__ Ram Ram
    in __init__ Ram Ram
    Hari Hari
    Ram Ram


If we were to return anything other than `instance` of object, then `__init__` function will never be called as shown in the below example.


```python
# Bad ideas of __new__ continued

class NewDistance(object):        
    def __new__(cls, dist):
        if dist != 22:
            print(cls)
            instance = object.__new__(cls)
            return instance
        else:
            print("in __new__", dist)
            return dist*0.0254

    def __init__(self, dist):    
        print("in __init__", dist)
        self.dist = dist

    def print_dist(self):
        print(self.__name__)
```


```python
try:
    mnt = NewDistance(22)
    print(mnt, type(mnt))
    mnt.print_dist()
except Exception as e:
    print(e)
```

    in __new__ 22
    0.5588 <class 'float'>
    'float' object has no attribute 'print_dist'



```python

try:
    mnt = NewDistance("test")
    print(mnt, type(mnt))
    mnt.print_dist()
except Exception as e:
    print(e)
```

    <class '__main__.NewDistance'>
    in __init__ test
    <__main__.NewDistance object at 0x0000000005640898> <class '__main__.NewDistance'>
    'NewDistance' object has no attribute '__name__'



```python
#class Distance(float):        
class Distance(object):
    def __new__(cls, dist):
        print("in __new__", dist)
        instance =  super(Distance, cls).__new__(cls)
        print(type(instance))
        instance.val = dist*0.0254
        return instance
    
    def __init__(self, dist):    
        print("in __init__", dist)
    
    def print_dist(self):
        print(self.val)
        

if __name__ == "__main__":
    try:
        mnt = Distance(22)
        print(mnt, type(mnt))
        mnt.print_dist()
    except Exception as e:
        print(e)
```

    in __new__ 22
    <class '__main__.Distance'>
    in __init__ 22
    <__main__.Distance object at 0x00000000056B2438> <class '__main__.Distance'>
    0.5588


### Where can we use `__new__`

#### Creating singleton class  

In singleton pattern, we create one instance of the class and all subsequent objects of that class points to the first instance.

Lets try to create a singleton class using `__new__` constructor.  


```python
class Godlike(object):  
    
    def __new__(cls, name):
        # __it__ is my custom attribute which I have creatd
        # to get the first instance (object) of the class
        if "__it__" in cls.__dict__:
            print("returning the existing object")
            return cls.__it__
        
        print("Creating the object")
        cls.__it__ = object.__new__(cls)
        return cls.__it__
    
    def __init__(self, name):
        """
        init function
        """
        print("Running init")
        self.name = name
    
    def print_name(self):
        print(self.name)
```


```python
ohm = Godlike("Ohm")
ram = Godlike("Ram")
hari = Godlike("Hari")
```

    returning the existing object
    Running init
    returning the existing object
    Running init
    returning the existing object
    Running init



```python
print(id(ohm), id(ram), id(hari))
```

    4561866704 4561866704 4561866704



```python
"""
To avoid multiple executions of __init__, we can move the functionality of it to another function (`init`)
"""
class Godlike(object):  
    
    def __new__(cls, name):
        # __it__ is my custom attribute which I have creatd
        # to get the first instance (object) of the class
        if "__it__" in cls.__dict__:
            print("returning the existing object")
            return cls.__it__
        
        print("Creating the object")
        cls.__it__ = object.__new__(cls)
        cls.__it__.init(name)
        return cls.__it__
    
    def init(self, name):
        """
        custom init which is manually 
        called in the constructor itself
        """
        print("inside init")
        self.name = name
    
    def print_name(self):
        print(self.name)
```


```python
ohm = Godlike("Ohm")
ram = Godlike("Ram")
hari = Godlike("Hari")
```

    Creating the object
    inside init
    returning the existing object
    returning the existing object



```python
print(ohm is ram)
print(ohm is hari)
```

    True
    True



```python
print("same id's for all", id(ohm), id(ram), id(hari))
```

    same id's for all 90072680 90072680 90072680



```python
ohm.print_name()
ram.print_name()
hari.print_name()
```

    Hari
    Hari
    Hari


Note, in the above example all three objects are pointing to same object `ohm` meaning all three objects are same. 

Now, we might have situations where we need to raise exception, if creation of more than one instance is attempted. We can achieve it by raising an exception as shown in below example.


```python
class SingletonError(Exception):
    pass

class HeadMaster(object):
    
    def __new__(cls, name):
        it = cls.__dict__.get("__it__")
        if it is not None:
            raise SingletonError(f"Count not create new instance for value {name}")
            
        cls.__it__ = it = object.__new__(cls)
        it.__init__(name)
        return it
    
    def __init__(self, name):        
        self.name = name
    
    def print_name(self):
        print(self.name)
        

try:
    print("Creating Anshu Mam as Primary School headmistress.")
    anshu_mam = HeadMaster("Anshu Shrivastava")
    anshu_mam.print_name()
    print("~"*20)
    
    print("Creating Rahim Sir as Primary School headmaster.")
    rahim_sir = HeadMaster("Rahim Khan")
except Exception as e:
    print(e)
```

    Creating Anshu Mam as Primary School headmistress.
    Anshu Shrivastava
    ~~~~~~~~~~~~~~~~~~~~
    Creating Rahim Sir as Primary School headmaster.
    Count not create new instance for value Rahim Khan


#### Regulating number of object creation

we are going to tweak previous example and convert it to have a finite number of objects created for the class


```python
class HeadMaster(object):
    __instances = []  # Keep track of instance reference
    __limit = 2

    def __new__(cls, *args, **kwargs):
        if len(cls.__instances) >= cls.__limit:
            raise RuntimeError("Creation Limit %s reached" % cls.__limit)
        
        instance = object.__init__(cls)
        cls.__instances.append(instance)
#         instance.__init__(*args, **kwargs)
        return instance
    
    def __init__(self, name):
        print("inside init")
        self.name = name

    def __del__(self):
        self.__instance.remove(self)
```


```python
try:
    li1 = HeadMaster("Gupta Sir")
    li2 = HeadMaster("Sharma Sir")
    print("2 object created ")
    li3 = HeadMaster("Tiwari Sir")
    print("3 object created ")
    li4 = HeadMaster()
except Exception as e:
    print("Exception:", e)
```

    2 object created 
    Exception: Creation Limit 2 reached



```python
print(li1, li2)
```

    None None



```python

```

#### Customize instance object

We can customize instance object using `__new__`

#### Customize Returned Object

As shown above, we can also return custom objects instead of instance of requested class as shown in one of the previous example.
