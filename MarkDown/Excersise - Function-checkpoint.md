
# Excersise - Function
Write a program to 
* Computes the result of x raised to the power of n
* Flattens a nested list, [ [1, 2, [3, 4] ], [5, 6], 7]

**  What is the output of the following **


```python
def func(i, x=[]):
    x.append(x.append(i))
    return x

y = 0
for i in range(10):
    y = func(i)
print(y)
```

    [0, None, 1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None]
    

 This set of Python Questions for entrance examinations focuses on “Functions”.

1. Which are the advantages of functions in python?
a) Reducing duplication of code
b) Decomposing complex problems into simpler pieces
c) Improving clarity of the code
d) Reuse of code
e) Information hiding
f) All of the mentioned


2. What are the two types of functions?
a) Custom function
b) Built-in function
c) User-Defined function
d) System function


3. Where is function defined?
a) Module
b) Class
c) Another function
d) None of the mentioned



4. What is called when a function is defined inside a class?
a) Module
b) Class
c) Another function
d) Method / attribute


5. Which of the following is the use of id() function in python?
a) Id returns the identity of the object
b) Every object doesn’t have a unique id
c) All of the mentioned
d) None of the mentioned


6. Which of the following refers to mathematical function?
a) sqrt
b) rhombus
c) add
d) rhombus


7. What is the output of below program?

    def cube(x):

        return x * x * x   

     

    x = cube(3)    

    print x

a) 9
b) 3
c) 27
d) 30


8. What is the output of the below program?

    def C2F(c):

        return c * 9/5 + 32

    print C2F(100)

    print C2F(0)

a) 212
32
b) 314
24
c) 567
98
d) None of the mentioned


9. What is the output of the below program?

    def power(x, y=2):

        r = 1

        for i in range(y):

           r = r * x

        return r

    print power(3)

    print power(3, 3)

a) 212
32
b) 9
27
c) 567
98
d) None of the mentioned


10. What is the output of the below program?

    def sum(*args):

       '''Function returns the sum 

       of all values'''

       r = 0

       for i in args:

          r += i

       return r

    print sum.__doc__

    print sum(1, 2, 3)

    print sum(1, 2, 3, 4, 5)

a) 6
15
b) 6
100
c) 123
12345
d) None of the mentioned

