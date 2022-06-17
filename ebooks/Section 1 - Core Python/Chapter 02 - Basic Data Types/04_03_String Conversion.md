
## String Conversion

### raw to Normal String


```python
import codecs

raw_str = r"Roshan Musheer's car is always\ntoo small for him. ;)"

print("raw string:", raw_str)

print(codecs.decode(raw_str, "unicode_escape"))
```

    raw string: Roshan Musheer's car is always\ntoo small for him. ;)
    Roshan Musheer's car is always
    too small for him. ;)


### Normal to raw 


```python
a = "Roshan Musheer's car is always\ntoo small for him. ;)"
print(a)
```

    Roshan Musheer's car is always
    too small for him. ;)



```python
print("%r" % a)
```

    "Roshan Musheer's car is always\ntoo small for him. ;)"


We can even store the raw string to a variable as shown in the below example. 


```python
x = "%r" % a
print(x)
```

    "Roshan Musheer's car is always\ntoo small for him. ;)"



```python
conf_path = "C:\new_apps\myapp\conf.conf"
print(conf_path)
```

    C:
    ew_apps\myapp\conf.conf



```python
raw_conf_path = "%r" % conf_path
print(raw_conf_path)
```

    'C:\new_apps\\myapp\\conf.conf'

