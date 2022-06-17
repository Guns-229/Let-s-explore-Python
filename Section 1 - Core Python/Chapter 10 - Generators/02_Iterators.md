
# Iterators

Iterators in Python are in abundance,
- All Generators
- Most Collection data type

Python iterator objects are required to support two methods while following the iterator protocol.

- `__iter__` returns the iterator object itself. This is used in for and in statements.

- `__next__` method returns the next value from the iterator. If there is no more items to return then it should raise `StopIteration` exception.

In this chapter we are going to cover only custom iterators as almost all other iterators have been taught in other sections.


```python
for a in range(10):
    print(a, end="  ")
```

    0  1  2  3  4  5  6  7  8  9  


```python
class MyRange(object):
    def __init__(self, ini_val=0, end_val=10, hop=1):
        self.__ini_val = ini_val
        self.__end_val = end_val
        self.__hop = hop
        self.__current_val = self.__ini_val
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__current_val >= self.__end_val:
            raise StopIteration
        else:
            val = self.__current_val
            self.__current_val += self.__hop 
            return val
```


```python
for a in MyRange(1, 22, 4):
    print(a, end=" ->")
print("\b\b")
```

    1 ->5 ->9 ->13 ->17 ->21 ->



```python
mt = MyRange(1, 4)

try:
    print(mt.__next__())
    print(mt.__next__())
    print(mt.__next__())
    print(mt.__next__(), ".")
except StopIteration as sie:
    print("Error:", sie)
```

    1
    2
    3
    Error: 



```python
class MyRange(object):
    def __init__(self, ini_val=0, end_val=10, hop = 1):
        self.ini_val = ini_val
        self.end_val = end_val
        self.hop = hop
        self.current_val = self.ini_val
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_val >= self.end_val:
            raise StopIteration
        else:
            val = self.current_val
            self.current_val += self.hop 
            return val
```
