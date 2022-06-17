
## Why Inheritance

 
- Gets rid of Code duplication 


## Single Inheritance

In single inheritance, any client class inherits from only one immediate parent class. Lets look at the below example which contains `Pen` as parent and `BallPen` & `InkPen` as clildren of it. 


```python
class Pen(object):
    """
    Should implement all the common features 
    """
    def __init__(self, size, name):
        self.name = name
        self.size = size
    
    def set_name(self, name):
        self.name = name


class BallPen(Pen):
    """
    Only the unique features should be implemented in child classes.
    """
    
    def __init__(self, size, name, color):
        self.color = color
        super().__init__(size, name)
    
    def set_color(self, color):
        self.color = color


class InkPen(Pen):
    def __init__(self, size, name, cart_type):
        self.cart = cart_type
        super().__init__(size, name)
```

`BallPen` & `InkPen` both are initializing the parent class using `super().__init(size, name)` function. Now lets create few objects of both,


```python
pb = BallPen(10, "Renolds", "Green")
print(pb.name)
pb.set_name("cello")
print(pb.name)
print(pb.__dict__)
```

    Renolds
    cello
    {'color': 'Green', 'name': 'cello', 'size': 10}



```python
ip = InkPen(size="10 cm", cart_type="2 MM", name="Renolds")
print(ip.name)
ip.set_name("cello")
print(ip.name)
print(ip.__dict__)
```

    Renolds
    cello
    {'cart': '2 MM', 'name': 'cello', 'size': '10 cm'}



```python
class grand_parent(object):
    def __init__(self, middle_name):
        print("grand_parent init")
        self.middle_name = middle_name
        
    def middle_name(self, middle_name):
        self.middle_name = middle_name
        return self.middle_name
```

Lets create a `parent` class which inherits `grand_parent` class, note we have used `super().__init__(middle_name)` to set middle name using parents function `middle_name`. 


```python
class parent(grand_parent):
    def __init__(self, middle_name, surname):
        print("parent init")
        self.surname = surname
        super().__init__(middle_name)
    
    def surname_name(self):
        return self.surname
```

Now lets create the `student` which inherits `parent` class. Check its init also. 


```python
class student(parent):
    def __init__(self, name, middle_name, surname):
        print("student init")
        self.name = name
        super().__init__(middle_name, surname)
        
    def test(self):
        # this will also fail use surname_name instead. 
        return self.surname
    
    def get_fullname(self):
        # Cannot directly access them,
        return F"{self.name} {self.middle_name} {self.surname}"
```


```python
mohan = student("Venkat", "kumar", "Mohan")
```

    student init
    parent init
    grand_parent init


Check the order of `init`'s being called. 


```python
print(mohan.middle_name)
```

    kumar



```python
mohan.middle_name = "KUMAR"
print(mohan.middle_name)
```

    KUMAR



```python
print(dir(mohan))
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_fullname', 'middle_name', 'name', 'surname', 'surname_name', 'test']



```python
print(mohan.test())
```

    Mohan


Now lets create the same classes without init functions, and see what happens


```python
class grand_parent:
    def __init__(self, middle_name):
        print("grand_parent init")
        self.middle_name = middle_name
        
    def middle_name(self, middle_name):
        self.middle_name = middle_name
        return self.middle_name

class parent(grand_parent):
    def __init__(self, middle_name, surname):
        print("parent init")
        self.surname = surname
    
    def middle_name(self):
        return self.middle_name
    
    
class student(parent):
    def __init__(self, name, middle_name, surname):
        print("student init")
        self.name = name
```


```python
mohan = student("Venkat", "kumar", "Mohan")
```

    student init



```python
try:
    print(mohan.middle_name())
except Exception as e:
    print(e)
```

    <bound method parent.middle_name of <__main__.student object at 0x107fabd10>>



```python
class A(object):
    def test(self, a):
        print("test", a)
        
class B(A):
    def testing(self, b):
        print("testing", b)
    
class C(B):
    def test_c(self, c):
        super().test(c)
        
c = C()
c.test_c("Hello")
```

    test Hello



```python
class A(object):
    def test(self, a):
        print("test", a)
        
class B(A):
    def testing(self, b):
        print("testing", b)
    
class C(B):
    def test_c(self, c):
        self.test(c)
        
c = C()
c.test_c("Hello")
```

    test Hello


### Why `super` when `self` can also do similar task

super can be called to explicitly call functions as shown in the below code. we are directly calling `A.test` and skipping `B.test` 


```python
class A(object):
    def test(self, a):
        print("test A", a)
        
class B(A):
    def test(self, b):
        print("test B", b)
    
class C(B):
    def test_c(self, c):
        super(B, self).test(c)
        
c = C()
c.test_c("Hello")
```

    test A Hello



```python
class A(object):
    def test(self, a):
        print("test A", a)
        
class B(A):
    def test(self, b):
        print("test B", b)
    
class C(B):
    def test_c(self, c):
        self.test(c)
        
c = C()
c.test_c("Hello")
```

    test B Hello



```python
class A(object):
    def test(self, a):
        print("test A", a)
        
class B(A):
    def test(self, b):
        print("test B", b)
    
class C(B):
    def test(self, c):
        super(B, self).test(c)
        
class D(C):
    def test(self, txt):
        super(C, self).test(txt)

    def test_b(self, txt):
        super(B, self).test(txt)
    
    def test_c(self, txt):
        super().test(txt)
d = D()
d.test("Testing")
d.test_b("Testing b")
d.test_c("testing c")
```

    test B Testing
    test A Testing b
    test A testing c



```python
# NOTE: python 2 has issues with Super , get it also documented here
```

### Class Private variable and inheritance

The PEP 8 Python Style Guide has this to say about private name mangling:

If your class is intended to be subclassed, and you have attributes that you do not want subclasses to use, consider naming them with double leading underscores and no trailing underscores. This invokes Python's name mangling algorithm, where the name of the class is mangled into the attribute name. This helps avoid attribute name collisions should subclasses inadvertently contain attributes with the same name.

Note 1: Note that only the simple class name is used in the mangled name, so if a subclass chooses both the same class name and attribute name, you can still get name collisions.

Note 2: Name mangling can make certain uses, such as debugging and  __getattr__(), less convenient. However the name mangling algorithm is well documented and easy to perform manually.

Note 3: Not everyone likes name mangling. Try to balance the need to avoid accidental name clashes with potential use by advanced callers.

Also PEP8 says

Use one leading underscore only for non-public methods and instance variables.

To avoid name clashes with subclasses, use two leading underscores to invoke Python's name mangling rules.

Python mangles these names with the class name: if class Foo has an attribute named `__a`, it cannot be accessed by `Foo.__a`. (An insistent user could still gain access by calling `Foo._Foo__a`.) Generally, double leading underscores should be used only to avoid name conflicts with attributes in classes designed to be subclassed.


```python
class Parent(object):
    def __init__(self, middle_name, surname):
        print("parent init")
        self.__surname = surname
        self.__middle_name = middle_name
    
    def surname(self):
        return self.__surname


class Student(Parent):
    def __init__(self, name, middle_name, surname):
        super().__init__(middle_name, surname)
        print("student init")
        self.name = name
    
    def full_name(self):
        print(self.name, self.__middle_name, self.__surname)
```


```python
sachin = Student("Janki", "Mohan", "Johri")
try:
    print(sachin.surname())
    sachin.full_name()
except Exception as e:
    print(e)
```

    parent init
    student init
    Johri
    'Student' object has no attribute '_Student__middle_name'



```python
class Student(Parent):
    def __init__(self, name, middle_name, surname):
        super().__init__(middle_name, surname)
        print("student init")
        self.name = name
    
    def full_name(self):
        print(self.name, super().__middle_name, super().__surname)
```


```python
sachin = Student("Janki", "Mohan", "Johri")
try:
    print(sachin.surname())
    sachin.full_name()
except Exception as e:
    print(e)
```

    parent init
    student init
    Johri
    'super' object has no attribute '_Student__middle_name'


So, you cannot directly access parents private variables, but only through parent class funcitons such as `surname`.


```python
# Lets use our hack to read private variables.
class Student(Parent):
    def __init__(self, name, middle_name, surname):
        super().__init__(middle_name, surname)
        print("student init")
        self.name = name
    
    def full_name(self):
        print(self.name, self._Parent__middle_name, self._Parent__surname)
```


```python
sachin = Student("Janki", "Mohan", "Johri")
try:
    print(sachin.surname())
    sachin.full_name()
except Exception as e:
    print(e)
```

    parent init
    student init
    Johri
    Janki Mohan Johri

