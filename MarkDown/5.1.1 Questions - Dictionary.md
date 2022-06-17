
# Questions - Dictionary
---

**Q: Which of the following statements create a dictionary?(multiple answers allowed)**

1. d = {}
2. d = {"mayank":40, "janki mohan johri":68}
3. d = {40:"mayank", 45:"janki mohan johri"}
4. d = (40:"mayank", 45:"janki mohan johri")

**Q: What will be the output of the followings**


```python
d = {"johri":40, "mayank":45}
print("johri" in d)
```


```python
d1 = {"johri":40, "mayank":45}
d2 = {"johri":466, "mayank":45}
print(d1 == d2)
```


```python
d1 = {"johri":40, "mayank":45}
d2 = {"johri":466, "mayank":45}
print(d1 != d2)
```

    True
    


```python
d1 = {"johri":40, "mayank":45}
d2 = {"johri":466, "mayank":45}
print(d1 < d2)
print(d1 > d2)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-1-b27d0a647056> in <module>()
          1 d1 = {"johri":40, "mayank":45}
          2 d2 = {"johri":466, "mayank":45}
    ----> 3 print(d1 < d2)
    

    TypeError: '<' not supported between instances of 'dict' and 'dict'



```python
d = {"johri":40, "mayank":45}
for a in d:
    print(type(a))

print(list(d))

for a, b in d.items():
    print(a, b)
```

    <class 'str'>
    <class 'str'>
    ['johri', 'mayank']
    johri 40
    mayank 45
    
