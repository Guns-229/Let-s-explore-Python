
# Interview Questions - Core Python

Detailed version of the "Interview Questions - Core Python" can be purchased from https://www.amazon.in/dp/B07BF7Q9C3

I have only recently started collecting the `Interview Questions for Core Python`. I will keep on adding more interview questions. 

I am also planning to pen a seperate ebook with details questions and solutions of them under the name of `FAQ's: Core Python`. It will be similar to one which I created for MSI Package & Repackaging (FAQ's:MSI Packaging & Repackaging").

## Basics 

- How to define Python code blocks
- What are the key features of Python?
- Please explain the `Python` execution flow
- Explain how Python does Compile-time and Run-time code checking
- What is the difference between .py and .pyc files
- What are the tools that help to find bugs or perform static analysis
- Is python a case sensitive language

## Variables

- Which of the following variable names are invalid and which are inappropriate
    - `_val`
    - `__val`
    - `_1val`
    - `1_val`
    - `val1`
    - `val1_`
    - `if`
    - `val_1`
    - `val 1`
    - `x-y-z`
    - `xyx_Z`
    - `XYZ`
    - `_`
    - `abc`
    - `in`

- Why `local` variable names should not begin with an underscore discouraged


```python

```

- what is the use of `_` variable

## Introspection

- What is the usage of help() and dir() function in Python

## Data Type

- List **built-in** type provided by python
- What is the maximum possible length of an identifier
- Why are local variable names beginning with an underscore discouraged
- How many kinds of sequences are supported by Python 3.x
- What is the use of enumerate() in Python
- What data type function `id` returns 


```python

```

### Numeric

- What is the type of `inf`

- What is the output of the followings  (using Python 3.x)
    
    - ```python
    float(‘nan’)
    ```
    - ```python
    print(round(2.5) - round(-10.5))
    ```
    - ```python
    print(round(0.50000000000001))
    ```
    - ```python
    print(0.3/(0.1 + 0.2))
    ```
    

- What is the output of the followings (using Python 2)
    
    - ```python
    float(‘nan’)
    ```
    - ```python
    print(round(2.5) - round(-10.5))
    ```
    - ```python
    print(round(0.50000000000001))
    ```

### String

- convert a number to a string
- What is docstring in Python
- How to capitalizes first letter of string
- How to make string an uppercase string
- How to change the string to lowercase string
- How to check in a string that all characters are digit
- How to check in a string that all characters are in lowercase
- How all to get the length of the string
- How to check is a substring is part of the string
- Remove all the leading and trailing whitespace in a string
- remove all the leading whitespace in a string
- remove all the trailing whitespace in a string
- Replace all the leading and trailing whitespace in a string with char `~`

- Create a banner with filling leading and trailing space with char `*`

- Find the number of times a text is present in a string

- What is the output of the followings
    - ```python 
    ['Roshan Musheer'] * 4
    ```
    - ```python 
    print("Hello, What are you doing', \"This is good")
    ```
    - ```python 
    print('Hello, What are you doing\', \"This is good\"')
    ```
    - ```python 
    a = " "
    b = "Rama"
    "Sri".join(a).join(b)
    ```
    - ```python 
    a = " "
    b = "Rama"
    "Sri".join(b).join(a)
    ```
    - ```python 
    a = "Sri"
    b = "Rama"
    b.join(a).join(" ")
    ```
    - ```python 
    a = "Sri"
    b = "Rama"
    b.join(" ").join(a)
    ```
    - ```python
    name = "Rigveda"
    name[3]="V"
    ```


```python

```

### List

- What is the difference between `list` and `tuple`
- Remove duplicates from a `list`
- How to reverse a `list`
- How to sort a `list`
- Are `del` and `remove` methods of `list` same
- How to get the max valued item of a list
- How to get the min valued item of a list
- Differentiate between append() and extend() methods in list.
- Insert an element at the given index in the list
- Join and sort two existing lists
- Obtain the index of an element in the list

- How to get the unique values from a list


```python
lst = [1, 2, 3, 44, 4, 2, 44, 55, 2, 34]
print(list(set(lst)))
```

    [1, 2, 3, 4, 34, 44, 55]


- Find the number of times a value is present in a list


```python
lst = [1, 2, 3, 44, 4, 2, 44, 55, 2, 34]
lst.count(2)
```




    3



- Find the unique words from the provided string 

- Split given text using multiple Delimiters


```python
# not using `re` as it has not be taught.
gita_txt = """The Supreme Lord is situated in everyone's heart, O Arjuna, 
                and is directing the wanderings of all living entities, 
                who are seated as on a machine, made of the material energy."""

sorted_txt = sorted(set(gita_txt.replace(',',' ').replace('\t',' ').replace('\n',' ').split(" ")))
print(sorted_txt)
```

    ['', 'Arjuna', 'Lord', 'O', 'Supreme', 'The', 'a', 'all', 'and', 'are', 'as', 'directing', 'energy.', 'entities', "everyone's", 'heart', 'in', 'is', 'living', 'machine', 'made', 'material', 'of', 'on', 'seated', 'situated', 'the', 'wanderings', 'who']



```python
# Check the `''` in the previous solution, we need to remove it. 
gita_txt = """The Supreme Lord is situated in everyone's heart, O Arjuna, 
                and is directing the wanderings of all living entities, 
                who are seated as on a machine, made of the material energy."""

sorted_txt = sorted(set(gita_txt.replace(",", ' ').replace('\n',' ').split(" ")))
sorted_txt.remove("")
print(sorted_txt)
```

    ['Arjuna', 'Lord', 'O', 'Supreme', 'The', 'a', 'all', 'and', 'are', 'as', 'directing', 'energy.', 'entities', "everyone's", 'heart', 'in', 'is', 'living', 'machine', 'made', 'material', 'of', 'on', 'seated', 'situated', 'the', 'wanderings', 'who']



```python
# using re module
# https://stackoverflow.com/questions/1059559/split-strings-with-multiple-delimiters

import re

s_list = sorted(set(re.split("[, \-!?:\n]+", gita_txt)))
print(s_list)
```

    ['Arjuna', 'Lord', 'O', 'Supreme', 'The', 'a', 'all', 'and', 'are', 'as', 'directing', 'energy.', 'entities', "everyone's", 'heart', 'in', 'is', 'living', 'machine', 'made', 'material', 'of', 'on', 'seated', 'situated', 'the', 'wanderings', 'who']


- What is the output of the followings
    - 
    ```python
    def listing(num, lst=[]):
        lst.append(num)
        return True
    
    l = [1, 2, 3]
    b = listing(10, l)
    print(b, l)
    ```
    - 
    ```python
    def listing(num, lst):
        lst.append(num)
        return True
    
    l = [1, 2, 3]
    b = listing(10, l)
    print(b, l)
    ```
    - 
    ```python
    def listing(num, lst=[]):
        lst.append(num)
        return True
    
    l = [1, 2, 3]
    b = listing([10], l)
    print(b, l)
    ```
    - 
    ```python
    def listing(num, lst=[]):
        lst.append(num)
        return True
    
    l = [1, 2, 3]
    b = listing([10], l)
    print(b, l)
    ```
    - 
    ```python
    101 in [101, 102, 103]
    ```
    - 
    ```python
    104 in [101, 102, 103]
    ```
    - ```python
    l = ["Mango", 'is', 'a', 'fruit']
    " ".join(l)
    ```

### Dictionary

- What is dictionary
- How to get all the keys from the dictionary
- How to get all the values from the dictionary
- How to get both key & value from the `dictionary` as `tuple` of `list`

- List all methods to dictionary be initialized using lists

- Create a dictionary using two list

- Create a dictionary from a list with key as position in list 

- Create a dictionary from a text file which contains unique words as keys and its occurrence as value


```python
# using open command to read the text file and store the value in `v_txt` variable
v_txt = """O nourisher, and enlightened person the policy which urges upon others the attainment of knowledge and
wealth is like a saw, that uphold the heart of people like you and spread good virtues far and near.

O teachers and preachers! you uphold kingdom or wealth every day (by your noble teachings), by the simile of illustration of the sun, you make firm the summit or the
advancement of the State, by whose association a man who is illuminator or instructor of all objects becomes firm and not decayinghaving
reached the earth and desirable knowledge, is increaser of the life, those who approach such a man and those (teachers and
preachers) ever enjoy happiness.

O men ! always have association with those teachers and preachers, who illuminate the dealirg of knowledge like the sun and increase kingdom, wealth and span of life and uphold
(establish) all in happiness. It is they by whose association, men become endowed with knowledge.
"""

words = v_txt.split()

# Lets create the dictionary with words, all the values has been defaulted to 0
v_dict = {}.fromkeys(words,0)

print(v_dict)
print("*"*20)
for w in words:
    v_dict[w] += 1
print(v_dict)
```

    {'O': 0, 'nourisher,': 0, 'and': 0, 'enlightened': 0, 'person': 0, 'the': 0, 'policy': 0, 'which': 0, 'urges': 0, 'upon': 0, 'others': 0, 'attainment': 0, 'of': 0, 'knowledge': 0, 'wealth': 0, 'is': 0, 'like': 0, 'a': 0, 'saw,': 0, 'that': 0, 'uphold': 0, 'heart': 0, 'people': 0, 'you': 0, 'spread': 0, 'good': 0, 'virtues': 0, 'far': 0, 'near.': 0, 'teachers': 0, 'preachers!': 0, 'kingdom': 0, 'or': 0, 'every': 0, 'day': 0, '(by': 0, 'your': 0, 'noble': 0, 'teachings),': 0, 'by': 0, 'simile': 0, 'illustration': 0, 'sun,': 0, 'make': 0, 'firm': 0, 'summit': 0, 'advancement': 0, 'State,': 0, 'whose': 0, 'association': 0, 'man': 0, 'who': 0, 'illuminator': 0, 'instructor': 0, 'all': 0, 'objects': 0, 'becomes': 0, 'not': 0, 'decayinghaving': 0, 'reached': 0, 'earth': 0, 'desirable': 0, 'knowledge,': 0, 'increaser': 0, 'life,': 0, 'those': 0, 'approach': 0, 'such': 0, '(teachers': 0, 'preachers)': 0, 'ever': 0, 'enjoy': 0, 'happiness.': 0, 'men': 0, '!': 0, 'always': 0, 'have': 0, 'with': 0, 'preachers,': 0, 'illuminate': 0, 'dealirg': 0, 'sun': 0, 'increase': 0, 'kingdom,': 0, 'span': 0, 'life': 0, '(establish)': 0, 'in': 0, 'It': 0, 'they': 0, 'association,': 0, 'become': 0, 'endowed': 0, 'knowledge.': 0}
    ********************
    {'O': 3, 'nourisher,': 1, 'and': 13, 'enlightened': 1, 'person': 1, 'the': 12, 'policy': 1, 'which': 1, 'urges': 1, 'upon': 1, 'others': 1, 'attainment': 1, 'of': 9, 'knowledge': 2, 'wealth': 3, 'is': 4, 'like': 3, 'a': 3, 'saw,': 1, 'that': 1, 'uphold': 3, 'heart': 1, 'people': 1, 'you': 3, 'spread': 1, 'good': 1, 'virtues': 1, 'far': 1, 'near.': 1, 'teachers': 2, 'preachers!': 1, 'kingdom': 1, 'or': 3, 'every': 1, 'day': 1, '(by': 1, 'your': 1, 'noble': 1, 'teachings),': 1, 'by': 3, 'simile': 1, 'illustration': 1, 'sun,': 1, 'make': 1, 'firm': 2, 'summit': 1, 'advancement': 1, 'State,': 1, 'whose': 2, 'association': 2, 'man': 2, 'who': 3, 'illuminator': 1, 'instructor': 1, 'all': 2, 'objects': 1, 'becomes': 1, 'not': 1, 'decayinghaving': 1, 'reached': 1, 'earth': 1, 'desirable': 1, 'knowledge,': 1, 'increaser': 1, 'life,': 1, 'those': 3, 'approach': 1, 'such': 1, '(teachers': 1, 'preachers)': 1, 'ever': 1, 'enjoy': 1, 'happiness.': 2, 'men': 2, '!': 1, 'always': 1, 'have': 1, 'with': 2, 'preachers,': 1, 'illuminate': 1, 'dealirg': 1, 'sun': 1, 'increase': 1, 'kingdom,': 1, 'span': 1, 'life': 1, '(establish)': 1, 'in': 1, 'It': 1, 'they': 1, 'association,': 1, 'become': 1, 'endowed': 1, 'knowledge.': 1}


- How to traverse a dictionary with sorted keys.


```python
my_dict = {"a" : 4, "b": 10, "12": 3, "d": 33, "1": 22}
for a in sorted(my_dict):
    print(a)
```

    1
    12
    a
    b
    d


### Slicing

- What are negative indexes and why are they used
- Describe indexing and slicing in details


- What is the output of the following print statements
    - ```python 
    p = "Manish"
    print(p[0:2]) 
    print(p[:2])
    print(p[1:4])
    print(p[-5:-2])
    print (p[::-1])
    print("implemented"[::-2])
    print("implemented"[-5::-2])
    print("implemented"[:-7:-2])
    print("implemented"[::2])
    print("implemented"[1::2])
    print("implemented"[1:4:2]) 
    ```
    - ```python
    x = "Mayank Johri"
    print(x)
    print("id(x)",id(x))
    print("x[0:]", id(x[0:]))
    print(id(x[1:]))
    print(id(x[2:]))
    print(x[0:])
    print(x[1:])
    print(x[2])
    ```

## Control Statements 

- What is the use of `continue` and `break`
- When will the else part of `while-else` be executed

### if

- what is the output of the follows
    - ```python
    name = "Sunil Kumar Bhele"
    lst = ["Sunil Kumar Bhele", "Rajeev", "Sachin", "Dhoke"]
    result = "DMS Alumni"  if name in lst else "Not"
    print(result)
    ```
    - ```python
    name = "Sunil Kumar Bhele"
    lst = ["Sunil Kumar Bhele", "Rajeev", "Sachin", "Dhoke"]
    if name in lst: print("DMS Alumni")
    ```    


```python

```

    DMS Alumni


## Scope 

- What is the difference between local and global namespaces
- Name the main types of namespaces in Python
- How to set value to a global variable
- How we are read the value of a global varialbe without using `global` keyword

## Functions 

- What does this mean: \*args, \*\*kwargs? And why would we use it
- Explain about Python's parameter passing mechanism
- What is lambda in Python
- what are local and global variables in Python

- what is the output of the follows:

    - ```python
    def test():
        pass
    d = test()
    print(d)
    ```
    - ```python
    def test():
        return "TEST", "Testing", True
    print(test())
    ```
    - ```python
    def test(txt, t):
        return (txt + '1') * t
    print(test("TEST", 2))
    ```

## OOPs

- What is a Class
- Explain the characteristics of Objects
- Define a protected member in a class
- Explain overload constructors or methods
- Explain Inheritance in Python
- How instance variables are different from class variables
- Which methods of Python are used to determine the type of instance and inheritance
- In a class, what `__ init__` function is used for
- How to compare two objects of the same class

## Modules

- What is a Python module
- What is namespace in Python
- What is module and package in Python
- Can modules be imported twice in a single program
- Name the four main types of namespaces in Python
- What is __init__.py used for
- How can `Global` variables be shared across modules

## Decorators

- Explain Python decorators

## Generators and iterators

- What are iterators
- What are generators

## Exception Handling 

- What are Exception Handling? How do you achieve it in Python?
- Explain different ways to raise exceptions
- Explain try: except: raise, and finally
- When will the else part of `try-except-else` be executed

## Standard library

- What is the difference between deep and shallow copy
- How can you generate random numbers in Python
- What kind of random items can be generated in Python
- Name the File-related modules in Python
- How to check the file existence and its extension
- Explain how to redirect the output of a python script from standout(ie., monitor) on to a file
- How to display the contents of text file in reverse order
- How can you copy an object in Python

- How is memory managed in Python

- Explain the use of `with` statement

## Operators

- How can the ternary operators be used in python

- what is the output of the followings:
    - ```python
    print(0.1 + 0.11 == 0.12)
    ```
    - ```python
    print(0.11 + 0.2 == 0.31)
    ```
    - ```python
    print(~1011)
    ```
    - ```python
    a = 10
    a = b
    ```
    - ```python
    5 + 2 //4
    ```
    - ```python
    5 + 2%4
    ```
    - ```python
    5 + 2%4
    ```
    - ```python
    5 + 2*4
    ```
    - ```python
    5 % 2*4 // 2
    ```
    - ```python
    int(5.55 % 2+3/3)
    ```
    - ```python
    round(5.55 % 2+3/3)
    ```

## Exceptions

- Describe the exception handling in python
- Write an example with all the following keywords `try: except: raise, finally`.

for more questions checkout my ebooks at Amazon: 
- "Frequently Asked Interview Questions : Core Python"
- "Frequently Asked Interview Questions : Advance Python"
