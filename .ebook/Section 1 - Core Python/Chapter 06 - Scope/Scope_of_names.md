
# Scope of names

The scope of names (variables) are maintained by **_Namespaces_**, which are dictionaries containing the names of the objects (references) and the objects themselves.

As we have seen that names are not pre-defined thus Python uses the code block of the assignment of a name to associate it with a particular namespace. In other words, the place where you assign a name in your source code determines its scope of visibility.

Python uses `lexical` scoping, which means that variable scopes are determined entirely by their locations in the source code and not by function calls. 

Rules for names inside **Functions** are as follows 

* Names assigned inside a `def` can only be seen by the code within that `def` and cannot be referred from outside the function.
* Names assigned inside a `def` do'nt clash with variables from outside the `def`. i.e. a name assigned outside a `def` is a completely different variable from a name assigned inside that `def`.
* If a variable is assigned outside all `defs`, then it is global to the entire file and can be accessed with the help of `global` keyword inside the `def`.


Normally, the names are defined in two dictionaries, which can be accessed through the functions `locals()` and `globals()`. These dictionaries are updated dynamically at <span class="note" title="Although the dictionaries returned by locals() and globals() can be changed directly, this should be avoided because it can have undesirable effects.">runtime</span>.



```python
month = 7 
year = 1947

def A():
    month = 3
    date = 10
    
def B():
    month = 2
#     date = 15
```

```python
month = 7 
year = 1947

def A():
    month = 3
    date = 10
    print(locals())
    print(globals())
    
def B():
    month = 2
    date = 15
    print(locals())
    print(globals())
    
A()
B()
```

**Output:**
    
```python
C02Q33EAFVH5:code mayank.johri$ python3 0_intro.py 
{'month': 3, 'date': 10}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x109c45f50>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '0_intro.py', '__cached__': None, 'month': 7, 'year': 1947, 'A': <function A at 0x109ce87a0>, 'B': <function B at 0x109ce8830>}
{'month': 2, 'date': 15}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x109c45f50>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '0_intro.py', '__cached__': None, 'month': 7, 'year': 1947, 'A': <function A at 0x109ce87a0>, 'B': <function B at 0x109ce8830>}

```


![Namespaces](files/scope_1.png)

Global variables can be overshadowed by local variables (because the local scope is consulted before the global scope). To avoid this, you must declare the variable as global in the local scope.

example:


```python
month = 7 
year = 1947

def A():
    month = 3
    date = 10
    print(month, date, year)
    
A()
print(month, year)
```

    3 10 1947
    7 1947



```python
month = 7
year = 1947

def A():
    global month
    month = 3
    date = 10
    print(month, date, year)
    
A()
print(month, year)
```

    3 10 1947
    3 1947



```python
month = 7 
year = 1947

def A():
    print("Month:", month)

A()
```

    Month: 7



```python
### !!! Gotcha's !!! 
month = 7 
year = 1947

def A():
    print("Month:", month)
    month = 3
    date = 10
    print(month, date, year)
    
try:
    A()
    print(month, year)
except Exception as e:
    print("Error:", e)
```

    Error: local variable 'month' referenced before assignment


### `globals` and `locals`


```python
# month = 7 
# year = 1947

# def A():
#     print("Month:", month)
#     print(locals())
#     print(globals())

# A()
```


```python
def test():
    """
    Updating the data
    """
    global glb
    print(glb)
    glb = 122

glb = 10    
test()
print(glb)
```

    10
    122



```python
def test():
    """
    Updating the data
    """
    global glb1
    print(glb)
    glb1 = 12

try:
    test()
    glb1 = 10
    print(glb1)
except Exception as e:
    print(e)
```

    122
    10



```python
def test():
    """
    Updating the data
    """
    global glb1
    glb1 = 12
    print(glb1)


test()
print(glb1)
```

    12
    12



```python
a = 10

def test():
    global a
    a = "Chennai Riders"
    print(a)
    a = "Pune Rocks"

test()
print(a)
```

    Chennai Riders
    Pune Rocks



```python
### Opps, we can change the values of global variables without 
#   using `global` keyword 

a = 100

def test():
    d = globals()
    d['a'] = 200

test()
print(a)
```

    200


#### Wasted global usage


```python
# please don't do the following, 
# Calling global keywork at module level does not help

global a
a = 10

def test():
    a = "Pune Rocks"
    print(a)
    print(locals())
    print("~"*20)
    
test()
print(a)
```

    Pune Rocks
    {'a': 'Pune Rocks'}
    ~~~~~~~~~~~~~~~~~~~~
    10



```python
# 1. At module level both locals and globals will return 
#    same values. 
# 2. when passed as argument, it do not get updated when 
#    we **assign** new value to it within the function

a = 10

def test(a):
    print(a)
    a = "Pune Rocks"
    print(locals())


test(a)
print(a)
print(len(locals()))
print(len(globals()))
```

    10
    {'a': 'Pune Rocks'}
    10
    39
    39



```python
# VERY VERY BAD Coding practice
# ** Assignation is the keyword

a = [10]

def test(a):
    print(a)
    print(locals())
    a = ["Pune Rocks"]
    print(locals())


test(a)
print(a)
print(len(locals()))
print(len(globals()))
```

    [10]
    {'a': [10]}
    {'a': ['Pune Rocks']}
    [10]
    41
    41



```python
# but if we update the values within the mutable data using one if its function, 
# then it will get reflected outside also because Python pass variables
# by reference instead of value.

a = [10]

def test():
    a.append("Pune Rocks")
    print(locals())

test()
print("A:", a)
print(len(locals()))
print(len(globals()))
```

    {}
    A: [10, 'Pune Rocks']
    44
    44



```python
# 1. At module level both locals and globals will return same values. 

a = 10

def test(a):
    print(a)
    a = "Pune Rocks"
    print(locals())
    return a
    
a = test(a)
print(a)
print(len(locals()))
print(len(globals()))
```

    10
    {'a': 'Pune Rocks'}
    Pune Rocks
    59
    59



```python
def addlist(lists):
    """
    Add lists of lists, recursively
    the result is global
    """
    global add
    
    for item in lists:
        if isinstance(item, list): # If item type is list
            addlist(item)
        else:
            add += item # add = add + item

add = 0
addlist([[1, 2], [3, [4, 5]], 6.29])

print(add)
```

    21.29



```python
# Gotcha: Trying to create a global variable inside the function 
# itself. 


def addlist(lists):
    """
    Add lists of lists, recursively
    the result is global
    """
    global add3
    
    for item in lists:
        if isinstance(item, list): # If item type is list
            addlist(item)
        else:
            try:
                add3 += item
            except NameError as ne:
                print("1: Error:", ne)
            
addlist([[1, 2], [3, 4, 5], 6])
try:
    print(add3)
except NameError as ne:
    print("2: Error:", ne)
```

    1: Error: name 'add3' is not defined
    1: Error: name 'add3' is not defined
    1: Error: name 'add3' is not defined
    1: Error: name 'add3' is not defined
    1: Error: name 'add3' is not defined
    1: Error: name 'add3' is not defined
    2: Error: name 'add3' is not defined



```python
# in this example we are creating a global variable inside the function 
# itself. 
del add2

def addlist(lists):
    """
    Add lists of lists, recursively
    the result is global
    """
    global add2
    
    for item in lists:
        if isinstance(item, list): # If item type is list
            addlist(item)
        else:
            # Checking if `add2` existing as global variable.
            if 'add2' in globals():
                add2 += item
            else:
                print("Creating add2 as global variable")
                add2 = item  

addlist([[1, 2], [3, 4, 5], 6])

print(add2)
```

    Creating add2 as global variable
    21


Using global variables is not considered a good development practice, as they make the system harder to understand, so it is better to avoid their use. The same applies to overshadowing variables.


```python
add = 10

def addlist(lists):
    """
    Add lists of lists, recursively
    the result is global
    """
    global add
    
    for item in lists:
        if isinstance(item, list): # If item type is list
            addlist(item)
            x = 100
        else:
            add += item


try:
    addlist([[1, 2], [3, 4, 5], 6])
except Exception as e:
    print(e)
print(add)
```

    31



```python
# Example 1: using outer function variables.
def outer():
    a = 0
    b = 10

    def inner():
        print(a)
        print(b)

    inner()

outer()
```

    0
    10


**NOTE:** A special quirk of Python is that – if no global statement is in effect – assignments to names always go into the innermost scope. Assignments do not copy data — they just bind names to objects.


```python
def outer():
    a = 0
    b = 1

    def inner():
        print(a)
        print(b)
        b = 4

    inner()
try:
    outer()
except Exception as e:
    print(e)
```

    0
    local variable 'b' referenced before assignment


```python
def outer():
    a = 0
    b = 1

    def inner():
        print(locals())
        print(globals())


    inner()
try:
    outer()
except Exception as e:
    print(e)
```

**Output:**
```python
$:> python scopes_in_innerfunctions.py
{}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_f
rozen_importlib_external.SourceFileLoader object at 0x0000000000690F98>, '__spec
__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>
, '__file__': 'scopes_in_innerfunctions.py', '__cached__': None, 'outer': <funct
ion outer at 0x0000000000641E18>}
```


```python
### Non Local

def outer():
    a = 11001
    b = 12002
    

    def inner():
        nonlocal a
        nonlocal b
        print("2:", id(a), id(b))
        a = 200000
        b = 400000
        print("3:", id(a), id(b))
        print(locals())

    print("1:", id(a), id(b))
    print(a, b)
    inner()
    print(a, b)
    print("4:", id(a), id(b))


try:
    outer()
except Exception as e:
    print(e)
```

    1: 4358512688 4358512720
    11001 12002
    2: 4358512688 4358512720
    3: 4357877072 4358512752
    {'a': 200000, 'b': 400000}
    200000 400000
    4: 4357877072 4358512752



```python
### !! Gotcha !!: Trying to declare global variable `b` as nonlocal
b = 1

def outer():
    a = 0

    def inner():
        nonlocal a
        nonlocal b
        a = 20
        b = 40        
        print(locals())

    print(a)
    print(b)
    inner()
    print(a)
    print(b)

try:
    outer()
except Exception as e:
    print(e)
```


      File "<ipython-input-10-cfcadaa5ebdd>", line 9
        nonlocal b
        ^
    SyntaxError: no binding for nonlocal 'b' found




```python
### Non Locals: gets the nearest available variables 
# as `a` we are getting from inner and `b` we are getting from `outer`
# Note: nonlocal will never search in globalvariales

def outer():
    a = 0
    b = 1  # non local variable for innermost

    def inner():
        """
            a: 20   `local` 
            b: 1    `non local` 
        """
        a = 20
        print("locals in `inner`:", locals())
        
        def innermost():
            nonlocal a, b
            print("locals in `innermost`:", locals())
            print(a, b)
            a, b = 20022, 11111
        
        print("Executing innermost")
        innermost()
        print("back in inner:", a, b)
        print("done executing")

    print("1:", a, b)
    inner()
    print(a, b)

try:
    outer()
except Exception as e:
    print(e)
```

    1: 0 1
    locals in `inner`: {'a': 20, 'b': 1}
    Executing innermost
    locals in `innermost`: {'a': 20, 'b': 1}
    20 1
    back in inner: 20022 11111
    done executing
    0 11111



```python
def power(x):
    def inner(y):
        return y ** x
    return inner

square = power(2)
cube = power(3)
```


```python
print(square)
print(cube)
```

    <function power.<locals>.inner at 0x103d138c0>
    <function power.<locals>.inner at 0x103d13950>



```python
square(10)
```




    100




```python
square(20)
```




    400




```python
cube(10)
```




    1000




```python
power(2)(20)
```




    400




```python
# VERY VERY VERY BAD EXample.
def List_fun(l, a=[]):
    """function takes 2 parameters list having values and empty list."""

    for i in l:
        #checking whether the values are list or not
        if isinstance(i, list):
            List_fun(i, a)
        else:
            a.append(i)
    return a 

b=[]
l2 = List_fun([[1, 2], [3, [4, 5]], 6, 7], b)
print(l2)
print(b)
print(id(l2))
print(id(b))
```

    [1, 2, 3, 4, 5, 6, 7]
    [1, 2, 3, 4, 5, 6, 7]
    4357625728
    4357625728



```python
def List_fun(l, a=[]):
    """function takes 2 parameters list having values and empty list."""
    
    for i in l:
        #checking whether the values are list or not
        if isinstance(i, list):
            List_fun(i, a)
        else:
            a.append(i)


b=[]
List_fun([[1,2],[3,[4,5]],6,7], b)
print(b)
```

    [1, 2, 3, 4, 5, 6, 7]



```python
# Gotcha: The changes are not retained outside the function
def fun_numbers(a):
    print(a, id(a))
    a += 10
    print(a, id(a))

b = 10
print(b, id(b))
fun_numbers(b)
print(b, id(b))
```

    10 4321234000
    10 4321234000
    20 4321234320
    10 4321234000



```python
# Better way to solve the case.
def fun_numbers(a):
    print(a, id(a))
    a += 10
    print(a, id(a))
    return a

b = 10
print(b, id(b))
b = fun_numbers(b)
print(b, id(b))
```

    10 4321234000
    10 4321234000
    20 4321234320
    20 4321234320



```python
# Gotcha: The changes are not retained outside the function

def fun_numbers(a):
    print(a)
    print(id(a))
    a = [20]
    print(a)
    print(id(a))

b = [10]
print(id(b))
fun_numbers(b)
print(b)
```

    4358367104
    [10]
    4358367104
    [20]
    4358397056
    [10]



```python
# Gotcha: Any updating the the multable data within the function 
# will be carry forwarded outside the function also .

def fun_numbers(a):
    print(a, id(a))
    a.append(20)
    print(a, id(a))

a = [10]

print(a, id(a))
fun_numbers(a)
print(a, id(a))
```

    [10] 4359130800
    [10] 4359130800
    [10, 20] 4359130800
    [10, 20] 4359130800



```python
def fun_numbers(a):
    print(a)
    a.append(120)
    print(a)

b = [10]
fun_numbers(b)
print(b)
```

    [10]
    [10, 120]
    [10, 120]



```python
def func():
    a = 10
    for d in [10,20,30]:
        a = a+d
    print(a)
    
func()
```

    70

