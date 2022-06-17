
# Custom Datatypes

## Custom Iterator


```python
class Counter():
    def __init__(self, large=1, small=0):
        self.large = large
        self.small = small
        self.num = small
    
    def __getitem__(self, key):
        if self.num < self.large:
            self.num +=1
        else:
            raise(IndexError)
        return self.num
        
```


```python
for i in Counter(2, 10):
    print(i)
```


```python
# generator
def uc_gen(text):
    for char in text:
        yield char.upper()

# generator expression
def uc_genexp(text):
    return (char.upper() for char in text)

# iterator protocol
class uc_iter():
    def __init__(self, text):
        self.text = text
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        try:
            result = self.text[self.index].upper()
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

# getitem method
class uc_getitem():
    def __init__(self, text):
        self.text = text
    def __getitem__(self, index):
        result = self.text[index].upper()
        return result
```


```python
for iterator in uc_gen, uc_genexp, uc_iter, uc_getitem:
    for ch in iterator('abcde'):
        print (ch, end="")
    print("")
```

    ABCDE
    ABCDE
    ABCDE
    ABCDE


## References
---

- https://stackoverflow.com/questions/19151/build-a-basic-python-iterator
