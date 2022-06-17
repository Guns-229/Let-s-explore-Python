
# Chapter 9: Scope of names
_____________________________

The scope of names in Python are maintained by **_Namespaces_**, which are dictionaries that list the names of the objects (references) and the objects themselves.

As we have seen that names are not pre-defined thus Python uses the code block of the assignment of a name to associate it with a particular namespace. In other words, the
place where you assign a name in your source code determines its scope of visibility.

Python uses `lexical` scoping, which means that variable scopes are determined entirely by their locations in the source code and not by function calls. 

Rules for names inside **Functions** are as follows 

* Names assigned inside a `def` can only be seen by the code within that `def` and cannot be referred from outside the function.
* Names assigned inside a `def` do'nt clash with variables from outside the `def`. i.e. a name assigned outside a `def` is a completely different variable from a name assigned inside that `def`.
* If a variable is assigned outside all `defs`, then it is global to the entire file and can be accessed with the help of `global` keyword inside the `def`.


Normally, the names are defined in two dictionaries, which can be accessed through the functions `locals()` and `globals()`. These dictionaries are updated dynamically at <span class="note" title="Although the dictionaries returned by locals() and globals() can be changed directly, this should be avoided because it can have undesirable effects.">runtime</span>.

![Namespaces](files/bpyfd_diags7.png)

Global variables can be overshadowed by local variables (because the local scope is consulted before the global scope). To avoid this, you must declare the variable as global in the local scope.

example:


```python
def addlist(lists):
    """
    Add lists of lists, recursively
    the result is global
    """
    global add
#     add = 0
    for item in lists:
#         print(item, "=>", add)
        if isinstance(item, list): # If item type is list
            addlist(item)
        else:
            add += item # add = add + item

add = 0
addlist([[1, 2], [3, 4, 5], 6])

print(add)
```

    21
    


```python
# add = 10

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
            if 'add2' in globals():
                add2 += item
            else:
                print("Creating add")
                add2 = 1

addlist([[1, 2], [3, 4, 5], 6])

print(add2)
```

    41
    

Using global variables is not considered a good development practice, as they make the system harder to understand, so it is better to avoid their use. The same applies to overshadowing variables.


```python
#add = 10

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
            
        print(x)

addlist([[1, 2], [3, 4, 5], 6])

print(add)
```


    ---------------------------------------------------------------------------

    UnboundLocalError                         Traceback (most recent call last)

    <ipython-input-3-0cd1c571bef2> in <module>()
         17         print(x)
         18 
    ---> 19 addlist([[1, 2], [3, 4, 5], 6])
         20 
         21 print(add)
    

    <ipython-input-3-0cd1c571bef2> in addlist(lists)
         10     for item in lists:
         11         if isinstance(item, list): # If item type is list
    ---> 12             addlist(item)
         13             x = 100
         14         else:
    

    <ipython-input-3-0cd1c571bef2> in addlist(lists)
         15             add += item
         16 
    ---> 17         print(x)
         18 
         19 addlist([[1, 2], [3, 4, 5], 6])
    

    UnboundLocalError: local variable 'x' referenced before assignment



```python
def outer():
    a = 0
    b = 1

    def inner():
        print(a)
        print(b)
        # b = 4

    inner()

outer()
```

    0
    1
    

**NOTE:** - A special quirk of Python is that – if no global statement is in effect – assignments to names always go into the innermost scope. Assignments do not copy data — they just bind names to objects.


```python
def outer():
    a = 0
    b = 1

    def inner():
        print(a)
        print(b)
        b = 4

    inner()

outer()
```

    0
    


    ---------------------------------------------------------------------------

    UnboundLocalError                         Traceback (most recent call last)

    <ipython-input-5-7d23a109e025> in <module>()
         10     inner()
         11 
    ---> 12 outer()
    

    <ipython-input-5-7d23a109e025> in outer()
          8         b = 4
          9 
    ---> 10     inner()
         11 
         12 outer()
    

    <ipython-input-5-7d23a109e025> in inner()
          5     def inner():
          6         print(a)
    ----> 7         print(b)
          8         b = 4
          9 
    

    UnboundLocalError: local variable 'b' referenced before assignment





```python

```
