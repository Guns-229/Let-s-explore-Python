
## <span style="color:Green">copy</span>: Shallow and deep copy operations

-----
In most of the programming languages assignment statement `=` equates to copy and thus are never in need of any other operator for creating a copy of an existing object. 

Lets start with exploring the assignment statement in python.

### Assignment ( = )

-----

**Assignments in Python do not copy objects, instead they create bindings between a target and the object**.


```python
x = 10
y = x
print(id(x), id(y))
```

    1722792688 1722792688
    


```python
x = [10, 3]
y = x
print(x , y)
x[1] = "This is a test message"
print(x, y)
```

    [10, 3] [10, 3]
    [10, 'This is a test message'] [10, 'This is a test message']
    


```python

```


```python
x = 10
print(id(x))
x +=1
y = x 
print(id(x), id(y))
```

    1722792688
    1722792720 1722792720
    


```python
x = 10
print(id(x))
y = x 
x = "d"
print(id(x), id(y))
print(y, x)
```

    1722792688
    2216063056280 1722792688
    10 d
    


```python

```


```python
x = "10"
y = x + "1"
print(id(x), id(y))
print(x , y)
```

    2216073178616 2216103588952
    10 101
    


```python
x = 10
y = x
print(id(x), id(y))
x = 111
print(id(x), id(y))
```

    1719909104 1719909104
    1719912336 1719909104
    


```python
x = [10, 20, 30]
y = x
print(id(x), id(y))
x[2] = 100
print(x, y)
```

    2160435348616 2160435348616
    [10, 20, 100] [10, 20, 100]
    

In the above example, x and y variables are pointing to same memory location and are two names to the same memory object, thus change in one will result in updating another value as long as they are not assigned to another memory location.
With that in mind lets explore the new example


```python
x = [10, 20, 30]
y = x
print(id(x), id(y))
x = 100
print(x, y)
print(id(x), id(y))
```

    2793410766024 2793410766024
    100 [10, 20, 30]
    1722795568 2793410766024
    


```python
x = ['a','b','c','d']
lst = [x, x]
print(x, lst)
x[2] = 'dd'
print(x, lst)
```

    ['a', 'b', 'c', 'd'] [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']]
    ['a', 'b', 'dd', 'd'] [['a', 'b', 'dd', 'd'], ['a', 'b', 'dd', 'd']]
    

#### Copy with the Slice Operator

Copying using slice can help us upto a certain level as shown in the below example


```python
x = ['a','b','c','d']
y = x[:2]
print(x, y)
# Good :)
print(id(x), id(y))
# but :(
print(id(x[1]), id(y[1]))
# thus 
x[1] = "33"
print(x, y)
# Good :)
print(id(x), id(y))
# but :(
print(id(x[1]), id(y[1]))
```

    ['a', 'b', 'c', 'd'] ['a', 'b']
    2216103555336 2216103506376
    2216064182512 2216064182512
    ['a', '33', 'c', 'd'] ['a', 'b']
    2216103555336 2216103506376
    2216103484864 2216064182512
    

but may will fail, if we have heterogeneous data-types in the list as shown in below examples


```python
x = [["a1", "b1", "c1"],'a','b','c','d']
y = x[:]
print(x, y)
# Good :)
print(id(x), id(y))
# but :(
print(id(x[0]), id(y[0]))
# thus 
x[0][1] = "33"
print(x, y)
# Good :)
print(id(x), id(y))
# but :(
print(id(x[1]), id(y[1]))
```

    [['a1', 'b1', 'c1'], 'a', 'b', 'c', 'd'] [['a1', 'b1', 'c1'], 'a', 'b', 'c', 'd']
    2160435277128 2160433650568
    2160435274504 2160435274504
    [['a1', '33', 'c1'], 'a', 'b', 'c', 'd'] [['a1', '33', 'c1'], 'a', 'b', 'c', 'd']
    2160435277128 2160433650568
    2162514259840 2162514259840
    

Now we now know that in Python **Assignment statements do not _copy objects_, instead they create bindings between a target and an object** and can't be used to create a copy of the existing object. 

Few More Examples for better understanding


```python

magic_list = [1,2,3]
print (magic_list)  
for i in magic_list:
    i = i+1
    print (i)
print (magic_list) 
```

    [1, 2, 3]
    2
    3
    4
    [1, 2, 3]
    


```python
magic_list = ["1","2","3"]
print (magic_list)  
for i in magic_list:
    i = i+str(1)
    print (i)
print (magic_list) 
```

    ['1', '2', '3']
    11
    21
    31
    ['1', '2', '3']
    


```python
lst1 = ['a','b',['ab','ba']]
print(id(lst1))
lst2 = lst1
print(id(lst2))
print(lst1)
print(lst2)
lst1[2][1] = "new"
print(lst1)
print(lst2)
lst1[0] = "new1"
print(lst1)
print(lst2)
lst1 = "as"
print(lst1)
print(lst2)

print(id(lst1))
print(id(lst2))
```

    2160435324680
    2160435324680
    ['a', 'b', ['ab', 'ba']]
    ['a', 'b', ['ab', 'ba']]
    ['a', 'b', ['ab', 'new']]
    ['a', 'b', ['ab', 'new']]
    ['new1', 'b', ['ab', 'new']]
    ['new1', 'b', ['ab', 'new']]
    as
    ['new1', 'b', ['ab', 'new']]
    2160398547856
    2160435324680
    


```python
x = 10
y = x
print(x)
print(y)
print(id(x))
print(id(y))
x = 11
print(id(x))
print(id(y))
```

    10
    10
    1719909104
    1719909104
    1719909136
    1719909104
    

<img src="files/shallowcopy1.png" width=300>

<img src="files/shallowcopy2.png" width=300>

<img src="files/shallowcopy3.png" width=470>

For collections which are mutable or contain mutable items, copy is sometimes needed so one can change one copy without changing the other. 
Fortunately we have This module provides generic shallow and deep copy operations called **`copy`**. 
It provides two functions, one for **shallow copy** and another for **deep copy**. 

### Shallow Copy - copy.copy(x)

**`Shallow copy` duplicates minimal possible**

`Shallow copy` of a collection is a copy of the collection structure, but not the elements. After shallow copy, both original and copied collection, share the individual elements.

Lets examine the below example for details


```python
import copy

class MyClass:
    def __init__(self, name): # contructor
        self.name = name
        
    def __cmp__(self, other):
        return cmp(self.name, other.name)

a = MyClass('a')
l = [ a ]
dup = copy.copy(l)

print ('l  :', l)
print ('dup:', dup)
print ('dup is l:', (dup is l))
print ('dup == l:', (dup == l))
print ('dup[0] is l[0]:', (dup[0] is l[0]))
print ('dup[0] == l[0]:', (dup[0] == l[0]))
```

    l  : [<__main__.MyClass object at 0x000001F703FB93C8>]
    dup: [<__main__.MyClass object at 0x000001F703FB93C8>]
    dup is l: False
    dup == l: True
    dup[0] is l[0]: True
    dup[0] == l[0]: True
    

Deep Copy - copy.deepcopy(x)

Return a deep copy of x.


```python
dup = copy.deepcopy(l)
print ('l  :', l)
print ('dup:', dup)
print ('dup is l:', (dup is l))
print ('dup == l:', (dup == l))
print ('dup[0] is l[0]:', (dup[0] is l[0]))
print ('dup[0] == l[0]:', (dup[0] == l[0]))
```

    l  : [<__main__.MyClass object at 0x000001F703FB93C8>]
    dup: [<__main__.MyClass object at 0x000001F703FCE400>]
    dup is l: False
    dup == l: False
    dup[0] is l[0]: False
    dup[0] == l[0]: False
    


```python
# shallow copy 
import copy

lst1 = ['a','b',['ab','ba']]
lst2 = copy.copy(lst1)

# print(id(lst1))
# print(id(lst2))
# print(lst1)
# print(lst2)
# lst1[2][1] = "new"
# print(lst1)
# print(lst2)
# lst1[0] = "new1"
# print(lst1)
# print(lst2)
# lst1 = "as"
# print(lst1)
# print(lst2)

print(id(lst1))
print(id(lst2))
print(id(lst1[1]))
print(id(lst2[1]))
print(lst1[1])
```

    2160434886472
    2160432920712
    2162514258160
    2162514258160
    b
    


```python
# shallow copy 
import copy

lst1 = ['a','b',['ab','ba']]
lst2 = copy.deepcopy(lst1)

print(id(lst1))
print(id(lst2))
print(lst1)
print(lst2)
lst1[2][1] = "new"
print(lst1)
print(lst2)
lst1[0] = "new1"
print(lst1)
print(lst2)
lst1 = "as"
print(lst1)
print(lst2)

# # print(id(lst3))
# print(id(lst4))
# print(id(lst3[1]))
# print(id(lst4[1]))
# print(lst3[1])
```

    2160433545928
    2160435348616
    ['a', 'b', ['ab', 'ba']]
    ['a', 'b', ['ab', 'ba']]
    ['a', 'b', ['ab', 'new']]
    ['a', 'b', ['ab', 'ba']]
    ['new1', 'b', ['ab', 'new']]
    ['a', 'b', ['ab', 'ba']]
    as
    ['a', 'b', ['ab', 'ba']]
    


```python
from copy import deepcopy

class person:
   def __init__ (this, name, background, age):
      this.name=name
      this.background=background
      this.age=age
   def setage (this,age):
      this.age = age
   def __str__(this):
      retst = this.name + "\nTrained as "
      retst += this.background + "\nAged "
      retst += str(this.age) + "\n"
      return retst
def tlist(source,demo):
   tl = demo + "\n"
   for pers in source:
      tl += str(pers)
   return tl

team = []
team.append(person("Lisa","Graphic Designer",21))
team.append(person("Graham","Support Manager",51))
team.append(person("Charlie","Unknown",9))

# firstyear is a clone of all levels of team - a full copy.
# Changes to team will NOT effect firstyear
firstyear = deepcopy(team)

# secondyear is a copy of all the team member references but
# not of the individual data for each team member. Changes to
# team will NOT effect secondyear, but changes to attributes
# of members within the team will.
secondyear = team[:]

# thirdyear is an alternative name for team, so any changes
# to team will also be changes to thirdyear.
thirdyear = team

print (tlist(team,"Original team"))
team[2] = person("Charlotte","Cat's home entertainer",10)
team[1].setage(53)
print (tlist(team,"Team after changes"))

print (tlist(firstyear,"Deep copy - no changes from original"))
print (tlist(secondyear,"Shallow copy - some changes"))
print (tlist(thirdyear,"Normal copy (alias) - all changes shown"))
```

    Original team
    Lisa
    Trained as Graphic Designer
    Aged 21
    Graham
    Trained as Support Manager
    Aged 51
    Charlie
    Trained as Unknown
    Aged 9
    
    Team after changes
    Lisa
    Trained as Graphic Designer
    Aged 21
    Graham
    Trained as Support Manager
    Aged 53
    Charlotte
    Trained as Cat's home entertainer
    Aged 10
    
    Deep copy - no changes from original
    Lisa
    Trained as Graphic Designer
    Aged 21
    Graham
    Trained as Support Manager
    Aged 51
    Charlie
    Trained as Unknown
    Aged 9
    
    Shallow copy - some changes
    Lisa
    Trained as Graphic Designer
    Aged 21
    Graham
    Trained as Support Manager
    Aged 53
    Charlie
    Trained as Unknown
    Aged 9
    
    Normal copy (alias) - all changes shown
    Lisa
    Trained as Graphic Designer
    Aged 21
    Graham
    Trained as Support Manager
    Aged 53
    Charlotte
    Trained as Cat's home entertainer
    Aged 10
    
    


```python

```

### Difference between shallow and deep copying

The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):

    A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
    A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

Two problems often exist with deep copy operations that don't exist with shallow copy operations:

    Recursive objects (compound objects that, directly or indirectly, contain a reference to themselves) may cause a recursive loop.
    Because deep copy copies everything it may copy too much, such as data which is intended to be shared between copies.

The deepcopy() function avoids these problems by:

    keeping a 'memo' dictionary of objects already copied during the current copying pass; and
    letting user-defined classes override the copying operation or the set of components copied.

### Controlling Copy Behavior

It is possible to control how copies are made using the __copy__ and __deepcopy__ hooks.

    __copy__() is called without any arguments and should return a shallow copy of the object.
    __deepcopy__() is called with a memo dictionary, and should return a deep copy of the object. Any member attributes that need to be deep-copied should be passed to copy.deepcopy(), along with the memo dictionary, to control for recursion (see below).

This example illustrates how the methods are called:


```python

import copy

class MyClass:
    def __init__(self, name):
        self.name = name
    def __cmp__(self, other):
        return cmp(self.name, other.name)
    def __copy__(self):
        print ('__copy__()')
        return MyClass(self.name)
    def __deepcopy__(self, memo):
        print ('__deepcopy__(%s)' % str(memo))
        return MyClass(copy.deepcopy(self.name, memo))

a = MyClass('a')

sc = copy.copy(a)
dc = copy.deepcopy(a)
```

    __copy__()
    __deepcopy__({})
    Wall time: 0 ns
    

## References

* http://www.python-course.eu/deep_copy.php
* http://www.shahmoradi.org/ECL2017S/lecture/5-python-variables-assignments
* https://medium.com/broken-window/many-names-one-memory-address-122f78734cb6
