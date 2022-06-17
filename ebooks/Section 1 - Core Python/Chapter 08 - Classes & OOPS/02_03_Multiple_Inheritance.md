
# Multiple Inheritance
---

In multiple inheritance, a `class` can be derived from more than one `base classes`. The syntax for multiple inheritance is similar to single inheritance except we list all the base classes in sequence instead of one base class in single inheritance.

```python
class ChildClass(<base_class_1>, <base_class_2>, ...):
    .... Child Class code 
```

Lets create few classes and expore the features of Multiple Inheritance.


```python
class Base1(object):
    pass

class Base2(object):
    pass

class MultiDerived(Base1, Base2):
    pass
```

Lets create the class `MultiDerived` child class using `Base1` & `Base2`. 


```python
md = MultiDerived()
print(md)
```

    <__main__.MultiDerived object at 0x10b1e2510>


The above object is a blank object with contains no custom defined attributes. Lets explore it in more details. 


```python
class Base1(object):
    def test(self, x):
        print("Base1", x)

class Base2(object):
    def test(self, x):
        print("Base2", x)

class MultiDerived(Base1, Base2):
    pass
```


```python
md = MultiDerived()
print(md.__dict__)
```

    {}



```python
print(md.__dir__())
```

    ['__module__', '__doc__', 'test', '__dict__', '__weakref__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']


observe that we have `test` function in the object, now the question is from which parent class it should inherit the `test` function.


```python
md.test(1999)
```

    Base1 1999


#### Static Variables


```python
class Base1(object):
    a = 10
    def test(self, x):
        print("Base1", x)

class Base2(object):
    a = 100
    def test2(self, x):
        print("Base2", x)

class MultiDerived(Base1, Base2):
    pass
```


```python
md = MultiDerived()
```


```python
print(dir(md))
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'test', 'test2']



```python
# intreasting observation.
print(md.a, md.__dict__)
```

    10 {}


Note only one `test` function


```python
class P1():
    def __init__(self):
        print("P-1 init")

class P2():
    def __init__(self):
        print("P-2 init")

class C1(P1, P2):
    pass

class C2(P2, P1):
    pass

c1 = C1()
print("*"*20)
c2 = C2()
```

    P-1 init
    ********************
    P-2 init


In the above example, we have created two child classes `C1` and `C2` with `P1`, `P2` and `P2`, `P1` as parents respectively. You will note that when we created child `c1` of class `C1`, as `C1` do not have any `__init__` function, Python searched it on parent classes, and executed & returned after finding its first definition, which it found in `P1` class, thus it did not ran the `__init__` of `P2`. Similarly `c2` ran the `__init__` of `P2` class. We will explain the algo which is used to find the required functions on parents later in the chapter. 


```python
class P1():
    pass

class P2():
    def __init__(self):
        print("P_2 init")

class C1(P1, P2):
    pass

class C2(P2, P1):
    pass

c1 = C1()
print("*"*20)
c2 = C2()
```

    P_2 init
    ********************
    P_2 init


Lets create a child class `TechLead` which is derived from `Lead` and `Tech` classes. 


```python
# Not a recommended way 
#**************************

class Tech(object):
    def __init__(self, tech):
        self._tech_name = tech
        
    @property
    def tech_name(self):
        return self._tech_name
    
    @tech_name.setter
    def tech_name(self, name):
        self._tech_name = name
        
class Lead(object):
    def __init__(self, reportee_count):
        self._reportee_count = reportee_count
    
    @property
    def reportee(self):
        return self._reportee_count
    
    @reportee.setter
    def reportee(self, count):
        self._reportee_count = count
        

class TechLead(Tech, Lead):
    def __init__(self, tech, count):
        # One way to call explicitly call specific parent function.
        Lead.__init__(self, count)
        Tech.__init__(self, tech)
        

vivek = TechLead("Nim Lang", 12)
print(vivek)
print(vivek.__dict__)
```

    <__main__.TechLead object at 0x10b4340d0>
    {'_reportee_count': 12, '_tech_name': 'Nim Lang'}


One issue with the above technique is that we might forget to add a parent class, which will results in issues which we might not be able to easily debug. 


Lets try the same using `super` function


```python
class Tech(object):
    def __init__(self, tech, **kwds):
        print("Inside Tech")
        self._tech_name = tech
        super().__init__(**kwds)
        
    @property
    def tech_name(self):
        return self._tech_name
    
    @tech_name.setter
    def tech_name(self, name):
        self._tech_name = name
        
class Lead(object):
    def __init__(self, count_reportee, **kwds):
        print("Inside Lead")
        self._reportee_count = count_reportee
        super().__init__(**kwds)
    
    @property
    def reportee(self):
        return self._reportee_count
    
    @reportee.setter
    def reportee(self, count):
        self._reportee_count = count
        

class TechLead(Tech, Lead):
    def __init__(self, name, **kwds):
        print("Inside TechLead")
        self._name = name
        super().__init__(**kwds)
```


```python
abhi = TechLead(name = "Abhishek Kumar",
                tech = "macOS",
                count_reportee = 10)
```

    Inside TechLead
    Inside Tech
    Inside Lead



```python
print(abhi)
print(abhi.__dict__)
```

    <__main__.TechLead object at 0x10b4415d0>
    {'_name': 'Abhishek Kumar', '_tech_name': 'macOS', '_reportee_count': 10}



```python
try:
    abhi = TechLead("Abhishek Kumar", "macOS", 10)
except Exception as e:
    print("Error:", e)
```

    Error: __init__() takes 2 positional arguments but 4 were given


#### Effects of missing `super().__init__(**kwds)`


```python
class Tech(object):
    def __init__(self, tech, **kwds):
        print("Inside Tech")
        self._tech_name = tech
#         super().__init__(**kwds)
        
    @property
    def tech_name(self):
        return self._tech_name
    
    @tech_name.setter
    def tech_name(self, name):
        self._tech_name = name
        
class Lead(object):
    def __init__(self, count_reportee, **kwds):
        print("Inside Lead")
        self._reportee_count = count_reportee
        super().__init__(**kwds)
    
    @property
    def reportee(self):
        return self._reportee_count
    
    @reportee.setter
    def reportee(self, count):
        self._reportee_count = count
        

class TechLead(Tech, Lead):
    def __init__(self, name, **kwds):
        print("Inside TechLead")
        self._name = name
        super().__init__(**kwds)
```


```python
abhi = TechLead(name="Abhishek Kumar", count_reportee=10, tech="macOS")
print(abhi)
print(abhi.__dict__)
```

    Inside TechLead
    Inside Tech
    <__main__.TechLead object at 0x10b44b550>
    {'_name': 'Abhishek Kumar', '_tech_name': 'macOS'}


Few things of importance you will find are as follows
- By adding `super().__init__(**kwds)` in all the parents `__init__` functions, and adding `super().__init__(**kwds)` in child `__init__` function, we can make sure that init of every parent is called automatically. 

- We can use similar to `def __init__(self, count_reportee, **kwds)` as `__init__` function signature, where `count_reportee` is the needed parameter for that class.


```python
# do not use it please.
class Tech(object):
    def __init__(self, tech, **kwds):
        print("Inside Tech")
        self._tech_name = tech
        super().__init__(**kwds)
        
    @property
    def tech_name(self):
        return self._tech_name
    
    @tech_name.setter
    def tech_name(self, name):
        self._tech_name = name
        
class Lead(object):
    def __init__(self, count_reportee, **kwds):
        print("Inside Lead")
        self._reportee_count = count_reportee
        super().__init__(**kwds)
    
    @property
    def reportee(self):
        return self._reportee_count
    
    @reportee.setter
    def reportee(self, count):
        self._reportee_count = count
        

class TechLead(Tech, Lead):
    def __init__(self, name, **kwds):
        print("Inside TechLead")
        self._name = name
        super().__init__(**kwds)
```


```python
abhi = TechLead("Abhishek Kumar", count_reportee=10, tech="macOS")
print(abhi)
print(abhi.__dict__)
```

    Inside TechLead
    Inside Tech
    Inside Lead
    <__main__.TechLead object at 0x10b434850>
    {'_name': 'Abhishek Kumar', '_tech_name': 'macOS', '_reportee_count': 10}


#### with using `*args`


```python
class Tech(object):
    def __init__(self, tech, *args):
        print("Inside Tech")
        self._tech_name = tech
        super().__init__(*args)
        
    @property
    def tech_name(self):
        return self._tech_name
    
    @tech_name.setter
    def tech_name(self, name):
        self._tech_name = name
        
class Lead(object):
    def __init__(self, count_reportee, *args):
        print("Inside Lead")
        self._reportee_count = count_reportee
        ## not recommended although no vidsible effects
        super().__init__(*args)
    
    @property
    def reportee(self):
        return self._reportee_count
    
    @reportee.setter
    def reportee(self, count):
        self._reportee_count = count
        

class TechLead(Tech, Lead):
    def __init__(self, name, *args):
        print("Inside TechLead")
        self._name = name
        super().__init__(*args)
```


```python
# Position matters when using positional arugments.
abhi = TechLead("Abhishek Kumar",  10, "macOS")
print(abhi)
print(abhi.__dict__)
```

    Inside TechLead
    Inside Tech
    Inside Lead
    <__main__.TechLead object at 0x10b452310>
    {'_name': 'Abhishek Kumar', '_tech_name': 10, '_reportee_count': 'macOS'}


Need to make sure that order in arguments in object creation is maintained otherwise issues like above will happen



```python
abhi = TechLead("Abhishek Kumar", "macOS", 10)
print(abhi)
print(abhi.__dict__)
```

    Inside TechLead
    Inside Tech
    Inside Lead
    <__main__.TechLead object at 0x10b452f90>
    {'_name': 'Abhishek Kumar', '_tech_name': 'macOS', '_reportee_count': 10}



```python
class Base1:
    def test(self):
        print("in Base1 -> test")

class Base2:
    def test(self):
        print("in Base2 -> test")

class MultiDerived(Base1, Base2):
    def test2(self):
        super().test()
        Base2.test(Base2)

class MultiDerived2(Base2, Base1):
    def test2(self):
        super().test()
        Base2.test(Base2)

print("Please check the result of test()")


md = MultiDerived()
md.test2()
md.test()
print("*"*10)
md2 = MultiDerived2()
md2.test2()
md2.test()
```

    Please check the result of test()
    in Base1 -> test
    in Base2 -> test
    in Base1 -> test
    **********
    in Base2 -> test
    in Base2 -> test
    in Base2 -> test


Note in the above example, when we created `c1` an object of `C1` and as `C1` class do not have initializing function `__init__` thus Python searched its parent   

## Multilevel Inheritance
---
we can inherit to from a derived class also. This is called as multilevel inheritance. Multilevel inheritance can be of any depth in Python. An example with corresponding visualization is given below.


```python
class Base(object):
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass
```

In the multiple inheritance scenario, any specified attribute is searched first in the current class. If not found, the search continues into parent classes in depth-first, left-right fashion without searching same class twice


```python
class Base:
    def test(self):
        print("In Base test")
    
    def test_alone(self):
        print("In Base test: test_alone")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")
        super().test()  # Calling parent function

    def test_alone(self, val):
        print("In Derived1 test: test_alone ", val)

    def test_alone(self):
        print("In Derived 1 test: test_alone without val")

class Derived2(Derived1):
    def test2(self):
        print("in Derived2 test2")
```


```python
obj = Derived2()
```


```python
obj.test()
obj.test2()
obj.test_alone()
# Focefully calling a function from a class
Base.test(Base)
```

    In Derived1 test
    In Base test
    in Derived2 test2
    In Derived 1 test: test_alone without val
    In Base test



```python
### Gotcha 1: Functions 

class Base:
    def test(self):
        print("In Base test")
    
    def test_alone(self):
        print("In Base test: test_alone")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")
        super().test()  # Calling parent function

    def test_alone(self, val):
        print("In Derived1 test: test_alone ", val)

#     def test_alone(self):
#         print("In Derived 1 test: test_alone without val")

class Derived2(Derived1):
    def test2(self):
        print("in Derived2 test2")
        
        
try:
    obj = Derived2()
    obj.test()
    obj.test2()
    obj.test_alone()
    # Focefully calling a function from a class
    Base.test(Base)
except Exception as e:
    print(e)
```

    In Derived1 test
    In Base test
    in Derived2 test2
    test_alone() missing 1 required positional argument: 'val'



```python
class Base:
    def test(self):
        print("In Base test")
    
    def test_base(self):
        print("test_base")

    def test_alone(self):
        print("In Base test: test_alone")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")
        super().test()
        self.test_base()
    
    def test_alone(self, val):
        print("In Derived1 test: test_alone ", val)
        self.test()

        
obj = Derived1()
obj.test()
obj.test_alone("test")
Base.test(Base)
```

    In Derived1 test
    In Base test
    test_base
    In Derived1 test: test_alone  test
    In Derived1 test
    In Base test
    test_base
    In Base test



```python
class Base:
    def test(self):
        print("In Base test")
    
    def test_base(self):
        print("test_base")

    def test_alone(self):
        print("In Base test: test_alone")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")
        super().test()
        Base.test_base(Base)
    
    def test_alone(self, val):
        print("In Derived1 test: test_alone ", val)
        self.test()

        
obj = Derived1()
obj.test()
obj.test_alone("test")
Base.test(Base)
```

    In Derived1 test
    In Base test
    test_base
    In Derived1 test: test_alone  test
    In Derived1 test
    In Base test
    test_base
    In Base test



```python
class Base:
    def test(self):
        print("In Base test")
        
    def test_alone(self):
        print("In Base test: test_alone")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")
        super().test()

    def test_alone(self, val):
        print("In Derived1 test: test_alone ", val)

    def test_alone(self):
        print("In Base test: test_alone")

class Derived2(Derived1):
    def test2(self):
        print("in Derived2 test2")
        
obj = Derived2()
obj.test()
obj.test2()
obj.test_alone()
Base.test(Base)
```

    In Derived1 test
    In Base test
    in Derived2 test2
    In Base test: test_alone
    In Base test



```python
class Base():
    def test1(self):
        print("In Base test")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")

class Derived3(Derived1):
    pass

d = Derived3()
d.test()
d.test1()
```

    In Derived1 test
    In Base test



```python
class Base():
    def test(self):
        print("In Base test")

class Derived1(Base):
    def test(self):
        print("In Derived1 test", end=", ")
        return "Golu"

class Derived3(Derived1):
    pass

d = Derived3()
print(d.test())
```

    In Derived1 test, Golu



```python
#### Explicitly calling function

class Base:
    def test(self):
        print("In Base test")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")

class Derived2(Derived1):
    pass

obj = Derived2
obj.test(obj)

Derived2.test(Derived2)
```

    In Derived1 test
    In Derived1 test



```python
#### Explicitly calling function

class Base:
    def test(self):
        print("In Base test")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")
        print(type(self))

class Derived2(Derived1):
    pass

obj = Derived2
obj.test(obj)

Derived2.test(Derived2)
```

    In Derived1 test
    <class 'type'>
    In Derived1 test
    <class 'type'>



```python
#### Explicitly calling function

class Base:
    def test(self):
        print("In Base test")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")
        print(type(self))

class Derived2(Derived1):
    pass


obj = Derived2()
obj.test()

Derived2.test(Derived2)
```

    In Derived1 test
    <class '__main__.Derived2'>
    In Derived1 test
    <class 'type'>



```python
# Position of `super()` in init also matters.
class CL1(object):
    def __init__(self):
        print ("class 1")
        super().__init__()
        print ("class 11")


class CL2(object):
    def __init__(self):
        print ("class 2")
        super().__init__()
        print ("class 22")


class CL3(CL1, CL2):
    def __init__(self):
        print ("class 3")
        super().__init__()
        print ("class 33")


instance = CL3()
```

    class 3
    class 1
    class 2
    class 22
    class 11
    class 33


### consistent method resolution

CMR is explained by Guido at [http://python-history.blogspot.com/2010/06/method-resolution-order.html](http://python-history.blogspot.com/2010/06/method-resolution-order.html). 

We will try to summerize it here.


```python
class A(object):
    def whereiam(self):
        print("I am in A")


class B(object):
    def whoiam(self):
        print("I am a method")


class C(A, B):
    pass
```


```python
c = C()
c.whoiam()
c.whereiam()
```

    I am a method
    I am in A



```python
class A(object):
    def whoiam(self):
        print("I am in A")


class B(object):
    def whoiam(self):
        print("I am in B")

class C(A, B):
    pass
```


```python
c = C()
c.whoiam()
```

    I am in A



```python
class A:
    def whereiam(self):
        print("I am in A")

class B(A):
    def whereiam(self):
        print("I am in B")

class C(A):
    def whereiam(self):
        print("I am in C")

class D(B, C):
    def whereiam(self):
        print("I am in D")
```


```python
d = D()
d.whereiam()
```

    I am in D



```python
class A:
    def whereiam(self):
        print("I am in A")

class B(A):
    def whereiam(self):
        print("I am in B")

class C(A):
    def whereiam(self):
        print("I am in C")

class D(B, C):
    pass
```


```python
d = D()
d.whereiam()
```

    I am in B



```python
class A:
    def whereiam(self):
        print("I am in A")

class B(A):
    pass

class C(A):
    def whereiam(self):
        print("I am in C")

class D(B, C):
    pass
```


```python
d = D()
d.whereiam()
```

    I am in C



```python
class A:
    def whereiam(self):
        print("I am in A")

class D:
    def whereiam(self):
        print("I am in D")

class B(A):
    pass

class C(D):
    def whereiam(self):
        print("I am in C")

class E(B, C):
    pass
```


```python
e = E()
e.whereiam()
```

    I am in C


### C3 Linearization Algorithm

C3 super-class linearization follow the following rules:

- Children precede their parents
- If a class inherits from multiple classes, they are kept in the order specified in the tuple of the base class.
- Consistent extended precedence graph, which in short means how base class is extended from the super class. Inheritance graph determines the structure of method resolution order.
- Preserving local precedence ordering, i.e., visiting the super class only after the method of the local classes are visited.
- Monotonicity


```python
class Type(type):
    def __repr__(cls):
        return cls.__name__

class O(object, metaclass=Type): pass


class A(O): pass

class B(O): pass

class C(O): pass

class D(O): pass

class E(O): pass

class K1(A, B, C): pass

class K2(D, B, E): pass

class K3(D, A): pass

class Z(K1, K2, K3): pass
```

`mro` returns the order in which the parent classes will be called to find the missing attribute.


```python
Z.mro()
```




    [Z, K1, K2, K3, D, A, B, C, E, O, object]



**Problem**

```python
class First(object):
    def __init__(self):
        print("first")

class Second(First):
    def __init__(self):
        print("second")

class Third(First, Second):
    def __init__(self):
        print("third")
```

```python
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-37-a1afb9897f3d> in <module>()
      7         print("second")
      8 
----> 9 class Third(First, Second):
     10     def __init__(self):
     11         print("third")

TypeError: Cannot create a consistent method resolution
order (MRO) for bases First, Second

```

- Solution


```python
## Avoid cyclic situations.

class First(object):
    def __init__(self):
        print("first")

class Second(First):
    def __init__(self):
        print("second")

class Third(Second):
    def __init__(self):
        print("third")
```


```python
Third.mro()
```




    [__main__.Third, __main__.Second, __main__.First, object]




```python
class O(object): pass

class A(O): pass

class B(O): pass

class C(O): pass

class D(O): pass

class E(O): pass

class K1(A, B, C): pass

class K2(D, B, E): pass

class K3(D, A): pass

class Z(K1, K2, K3): pass
```


```python
print(Z.mro())
```

    [<class '__main__.Z'>, <class '__main__.K1'>, <class '__main__.K2'>, <class '__main__.K3'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.E'>, <class '__main__.O'>, <class 'object'>]


## Finding subclasses using `__subclasses__()`


```python
class O(object): pass

class A(O): pass

class B(O): pass

class C(O): pass

class D(O): pass

class E(O): pass

class K1(A, B, C): pass

class K2(D, B, E): pass

```


```python
O.__subclasses__()
```




    [__main__.A, __main__.B, __main__.C, __main__.D, __main__.E]



thus, we can create the following code the get the `sub-classes` name


```python
print([cls.__name__ for cls in O.__subclasses__()])
```

    ['A', 'B', 'C', 'D', 'E']


Lets create a small function based on the above code sample


```python
def get_subclasses(cls):
    lst = []
    for a in cls.__subclasses__():
        lst.append(a)
        lst.extend(get_subclasses(a))
    return set(lst)
        
get_subclasses(O)
```




    {__main__.A,
     __main__.B,
     __main__.C,
     __main__.D,
     __main__.E,
     __main__.K1,
     __main__.K2}



## References

- https://en.wikipedia.org/wiki/C3_linearization
