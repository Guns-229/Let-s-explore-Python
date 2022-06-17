
# Multiple Inheritance
---
Multiple inheritance is possible in Python unlike other programming languages. A class can be derived from more than one base classes. The syntax for multiple inheritance is similar to single inheritance.


```python
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
```


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
#     def __init__(self):
#         print("Hello MultiDerived")

class MultiDerived2(Base2, Base1):
    pass

print("Please check the result of test()")

d = Base2()
# print(type(d))
md = MultiDerived()
md.test2()
# md.test()
# print(type(md))

# md2 = MultiDerived2
# md2.test(md2)
```

    Please check the result of test()
    in Base1 -> test
    in Base2 -> test
    

## Multilevel Inheritance
---
we can inherit to from a derived class also. This is called as multilevel inheritance. Multilevel inheritance can be of any depth in Python. An example with corresponding visualization is given below.


```python
class Base:
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

class Derived1(Base):
    def test(self):
        print("In Derived1 test")

class Derived2(Derived1):
    def test2(self):
        print("in Derived2 test2")
        super().test()
    pass
    

obj = Derived2()
obj.test()
obj.test2()
```

    In Derived1 test
    in Derived2 test2
    


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-55-9a73c3ab2539> in <module>()
         16 obj = Derived2()
         17 obj.test()
    ---> 18 obj.test2()
    

    <ipython-input-55-9a73c3ab2539> in test2(self)
         10     def test2(self):
         11         print("in Derived2 test2")
    ---> 12         super().super().test()
         13     pass
         14 
    

    AttributeError: 'super' object has no attribute 'super'



```python
class Base():
    def test(self):
        print("In Base test")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")

class Derived3(Derived1):
    pass

d = Derived3()
print(d.test())
```

    In Derived1 test
    None
    


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

```
