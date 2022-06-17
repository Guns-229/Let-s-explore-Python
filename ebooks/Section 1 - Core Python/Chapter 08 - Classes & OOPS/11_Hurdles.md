
**Hurdle 1: What will the output of the following program.**


```python
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())
```

    A B
    A B



```python
class Circle(object):
    color = "red"

class NewCircle(Circle):
    color = "blue"
    
nc = NewCircle
print(nc)
```

    <class '__main__.NewCircle'>



```python
print(nc.color)
```

    blue



```python
class Person:
    def __init__(self, id):
        self.id = id
 
sam = Person(100)
 
sam.__dict__['age'] = 49
print (sam.age + len(sam.__dict__))
```

    51



```python
class A:
    def __init__(self):
        self.calc_i(30)
        print("i from A is", self.i)
 
    def calc_i(self, i):
        self.i = 2 * i;
 
class B(A):
    def __init__(self):
        super().__init__()
        
    def calc_i(self, i):
        self.i = 3 * i;
 
b = B()
```

    i from A is 90



```python

```


```python

```
