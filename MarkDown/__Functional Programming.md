
# Basics of Functional code
---
* Functions are first­class ­­ You can store them in a structure, pass them to a function, and return them from a function. 
* Function calls can take keyword arguments. 
Example: 
> test(size=25) 
* Formal parameters to a function can have default values. 
Example: 
> def test(size=0): ... 
* Do not use mutable objects as default values. You can "capture" remaining arguments with *args, and **kwargs. (Spelling is not significant.)


```python
map(do_it, [f1, f2])
hello = lambda first, last: print("Hello", first, last)
bye = lambda first, last: print("Bye", first, last)
_ = list(map(do_it, [hello, bye], ['David','Jane', 'Mayank'], ['Mertz','Doe', 'Johri']))
```

    Hello David Mertz
    Bye Jane Doe
    


```python

```


```python

```
