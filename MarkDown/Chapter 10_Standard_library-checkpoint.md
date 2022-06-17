
## Chapter 10 : Standard Library
_____________________________
It's often said that Python comes with **"batteries included"**, in reference to the vast library of modules and packages that are distributed with the interpreter.

Some important modules of the standard library:
+ Math: math, cmath, and random decimal.
+ System: os, glob, subprocess and shutils.
+ Threads: threading.
+ Persistence: pickle and cPickle.
+ XML: xml.dom, xml.sax and ElementTree (since version 2.5).
+ Configuration: ConfigParser and optparse.
+ Time: time and datetime.
+ Other: sys, logging, traceback, types and timeit.

Maths
----------
In addition to the *builtin* numeric types in the Python standard library, there are several modules devoted to implementing other types and mathematical operations.

The *math* module defines logarithmic, exponentiation, trigonometric, and hyperbolic functions, as well as angular conversions and more. The *cmath* module implements similar functions, but can handle complex numbers.

Example:


```python
import math

import cmath

# Complex
for cpx in [3j, 1.5 + 1j, -2 - 2j]:

    # Polar coordinate conversion
    plr = cmath.polar(cpx)
    print ('Complex:', cpx)
    print ('Polar:', plr, '(in radians)')
    print ('Amplitude:', abs(cpx))
    print ('Angle:', math.degrees(plr[1]), '(grades)')
```

    Complex: 3j
    Polar: (3.0, 1.5707963267948966) (in radians)
    Amplitude: 3.0
    Angle: 90.0 (grades)
    Complex: (1.5+1j)
    Polar: (1.8027756377319946, 0.5880026035475675) (in radians)
    Amplitude: 1.8027756377319946
    Angle: 33.690067525979785 (grades)
    Complex: (-2-2j)
    Polar: (2.8284271247461903, -2.356194490192345) (in radians)
    Amplitude: 2.8284271247461903
    Angle: -135.0 (grades)
    

The *random* module brings functions for random number generation.

Examples:


```python
import random
import string

# Choose a letter
# print (string.ascii_uppercase)
# print(help(random))
print (random.choice(string.ascii_uppercase))



# Choose a number from 1 to 10
x = random.randrange(1, 100)
print (x)

# Choose a float from 0 to 1
print (random.random()*100)
```

    G
    78
    58.707671513360374
    


```python
lst = ["a", "b", "c", "e"]
dirs ={}

for  l in lst:
    dirs[l] = random.randrange(1, 100)

print(dirs)
```

    {'a': 59, 'b': 49, 'c': 53, 'e': 4}
    

In the standard library there is the decimal module that defines operations with real numbers with fixed precision.

Example:


```python
from decimal import Decimal

t = 5.
for i in range(50):
    t = t - 0.1

print ('Float:', t)

t = Decimal('5.')
for i in range(50):
    t = t - Decimal('0.1')

print ('Decimal:', t)
```

    Float: 1.0269562977782698e-15
    Decimal: 0.0
    

With this module, it is possible to reduce the introduction of rounding errors arising from floating point arithmetic.

In version 2.6, the module *fractions*, which deals with rational numbers,  is also available.

Example:


```python
from fractions import Fraction

# Three fractions
f1 = Fraction('-2/3')
f2 = Fraction(3, 4)
f3 = Fraction('.25')
print ("Fraction('-2/3') =", f1)
print ("Fraction('3, 4') =", f2)
print ("Fraction('.25') =", f3)

# Sum
print (f1, '+', f2, '=', f1 + f2)
print (f2, '+', f3, '=', f2 + f3)
```

    Fraction('-2/3') = -2/3
    Fraction('3, 4') = 3/4
    Fraction('.25') = 1/4
    -2/3 + 3/4 = 1/12
    3/4 + 1/4 = 1
    

Fractions can be initialized in several ways: as a *string*, as a pair of integers, or as a real number. The module also has a function called `gcd()` which calculates the greatest common divisor (gcd) of two integers.

Files and I/O
--------------
Files in Python are represented by objects of type <span class="note" title="the reference open points to file">*file*</span>, which offer various methods for file operations. Files can be opened for reading ('r', which is the default), writing ('w'), or appending ('a'), in text or binary ('b') mode.

In Python:

+ *sys.stdin* is the standard input.
+ *sys.stdout* is the standard output.
+ *sys.stderr* is the standard error output.

The standard input, output and error are handled by Python as open files. The input in read mode and the other in the recording mode.

Sample of writing:


```python
# The old way .... the C,C++ etc way
import sys

# Create an object of type file
temp = open('temp.txt', 'w')

# Write output
for i in range(20):
    temp.write('%03d\n' % i)

temp.close()

temp = open('temp.txt')
temp1 = open('temp1.txt')

# Write in terminal
for x in temp:
    # writing in sys.stdout sends
    # text to standard output
    print("x")
    sys.stdout.write(x)
    temp1.write(x)

temp.close()
temp1.close()
```

    x
    000
    x
    001
    x
    002
    x
    003
    x
    004
    x
    005
    x
    006
    x
    007
    x
    008
    x
    009
    x
    010
    x
    011
    x
    012
    x
    013
    x
    014
    x
    015
    x
    016
    x
    017
    x
    018
    x
    019
    


```python
#  Python way
import sys

# Create an object of type file
with open('temp.txt', 'w') as temp:
    # Write output
    for i in range(20):
        temp.write('%03d\n' % i)
# temp.close()

with open('temp.txt') as temp:
    # Write in terminal
    for x in temp:
        # writing in sys.stdout sends
        # text to standard output
        sys.stdout.write(x)

#temp.close()
```

    000
    001
    002
    003
    004
    005
    006
    007
    008
    009
    010
    011
    012
    013
    014
    015
    016
    017
    018
    019
    


```python
# print(help(open))
```

At each iteration in the second loop, the object returns a line from the file each time.

Reading example:


```python
import sys
import os.path

fn = 'temp2.txt'

if not os.path.exists(fn):
    print ('Try again...')
    sys.exit(0)

# Numbering lines
for i, s in enumerate(open(fn)):
    print (i + 1, s),
```

    Try again...
    


    An exception has occurred, use %tb to see the full traceback.
    

    SystemExit: 0
    


    C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\lib\site-packages\IPython\core\interactiveshell.py:2889: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
      warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)
    

It is possible to read all the lines with the method `readlines()`:


```python
# Prints a list with all the lines from a file
print (open('temp.txt').readlines())
```

    ['000\n', '001\n', '002\n', '003\n', '004\n', '005\n', '006\n', '007\n', '008\n', '009\n', '010\n', '011\n', '012\n', '013\n', '014\n', '015\n', '016\n', '017\n', '018\n', '019\n']
    


```python

print (len(open('temp.txt').readlines())) # 20
print(len(open('temp.txt').read())) # 4x20
```

    20
    80
    

File Systems
-------------------
Modern operating systems store files in hierarchical structures called *file systems*.

Several features related to file systems are implemented in the module *os.path*, such as: 

+ `os.path.basename()`: returns the final component of a path.
+ `os.path.dirname()`: returns a path without the final component.
+ `os.path.exists()`: returns *True* if the path exists or *False* otherwise.
+ `os.path.getsize()`: returns the size of the file in *bytes*.

*glob* is another module related to the file system:


```python
# print(help(os.path))
```


```python
import os.path 

a = r"c:\users\mayank"
b = r"warzone\myprogram.conf"
c = os.path.join(a,b)
print(c)
print(os.path.split(c))
print(os.path.splitext(c))
print(os.path.splitdrive(c))

```

    c:\users\mayank\warzone\myprogram.conf
    ('c:\\users\\mayank\\warzone', 'myprogram.conf')
    ('c:\\users\\mayank\\warzone\\myprogram', '.conf')
    ('c:', '\\users\\mayank\\warzone\\myprogram.conf')
    


```python
import os.path
import glob

# Shows a list of file names
# and their respective sizes 
for arq in sorted(glob.glob('*.*')):
    print (arq, os.path.getsize(arq))
```

    Chapter 10_Standard_library.ipynb 31449
    arq.zip 189
    arq1.zip 189
    dt.csv 70
    eggs.csv 77
    temp.txt 100
    

The *glob.glob()* function returns a list of filenames that meet the criteria passed as a parameter in a similar way to the `ls` command available on UNIX systems.

Temporary files
--------------------
The module *os* implements some functions to facilitate the creation of temporary files, freeing the developer from some concerns, such as:

+ Avoiding collisions with names of files that are in use.
+ Identifying the appropriate area of the file system for temporary files (which varies by operating system).
+ Not exposing the implementation risks (temporary area is used by other processes).

Example:


```python
import tempfile

# create a temporary file and write some data to it
fp = tempfile.TemporaryFile()
fp.write(b'Hello world!')
# read data from file
fp.seek(0)
fp.read()

# close the file, it will be removed
fp.close()

# create a temporary file using a context manager
with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    fp.read()

# file is now closed and removed

# create a temporary directory using the context manager
with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)

# directory and contents have been removed
```

    created temporary directory C:\Users\johri_m\AppData\Local\Temp\tmp6t64qfxu
    

The objects of type file also have the method `seek()`, which allow going to any position in the file.


```python
# print(help(type(fp)))
```

There is also the `tempnam()` function, which returns a valid name for temporary file, including a path that respects the conventions of the operating system. However, it is up to the developer to ensure that the routine is used so as not to compromise the security of the application.

Compressed files
--------------------
Python has modules to work with multiple formats of compressed files.

Example of writing a ".zip" file:


```python
"""
Writing text in a compressed file
"""

import zipfile

text = """
**************************************
This text will be compressed and ...
... stored inside a zip file.
***************************************
"""

# Creates a new zip
zip = zipfile.ZipFile('arq1.zip', 'w',
    zipfile.ZIP_DEFLATED)

# Writes a string in zip as if it were a file
zip.writestr('text.txt', text)
zip.writestr('text1.txt', text)
zip.writestr('text2.txt', text)
# closes the zip
zip.close()
```

Reading example:


```python
"""
Reading a compressed file
"""
import zipfile

# Open the zip file for reading 
zip = zipfile.ZipFile('arq1.zip')

# Gets a list of compressed files
arqs = zip.namelist()

for arq in arqs:
    # Shows the file name
    print ('File:', arq)
    # get file info
    zipinfo = zip.getinfo(arq)
    print ('Original size:', zipinfo.file_size)
    print ('Compressed size:', zipinfo.compress_size)

    # Shows file content
    print (zip.read(arq))
```

    File: text.txt
    Original size: 147
    Compressed size: 75
    b'\n**************************************\nThis text will be compressed and ...\n... stored inside a zip file.\n***************************************\n'
    File: text1.txt
    Original size: 147
    Compressed size: 75
    b'\n**************************************\nThis text will be compressed and ...\n... stored inside a zip file.\n***************************************\n'
    File: text2.txt
    Original size: 147
    Compressed size: 75
    b'\n**************************************\nThis text will be compressed and ...\n... stored inside a zip file.\n***************************************\n'
    

Python also provides modules for gzip, bzip2 and tar formats that are widely used in UNIX environments.

Data file
----------------
In the standard library, Python also provides a module to simplify the processing of files in CSV (*Comma Separated Values*) format.

In CSV format, the data is stored in text form, separated by commas, one record per line.

Writing example:


```python
import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
```


```python
lst = [["a", "a1"], ["b", "b1"], ["d", "d1 ,one"], "c", "f" ]
with open('list.csv', 'w', newline='') as csvfile:
    listWriter = csv.writer(csvfile)
    for l in lst:
        listWriter.writerow(l)
```

Reading example:


```python
import csv

with open("eggs.csv", newline='') as csvfile:
    for row in csv.reader(csvfile, delimiter=' ', quotechar='|'):
        print(', '.join(row))
```

    Spam,Spam,Spam,Spam,Spam,Baked, Beans
    Spam,Lovely, Spam,Wonderful, Spam
    

The CSV format is supported by most spreadsheet and databases for data import and export.

Operating System
-------------------
Apart from the file system, the modules of the standard library also provides access to other services provided by the operating system.

Example:


```python
import os
import sys
import platform

def uid():
    """
    uid() -> returns the current user identification
    or None if not possible to identify
    """

    # Ambient variables for each operating system
    us = {'Windows': 'USERNAME',
        'Linux': 'USER'}

    u = us.get(platform.system())
    return os.environ.get(u)

print ('User:', uid())
print ('plataform:', platform.platform())
print ('Current dir:', os.path.abspath(os.curdir))
exep, exef = os.path.split(sys.executable)
print ('Executable:', exef)
print ('Executable dir:', exep)
```

    User: johri_m
    plataform: Windows-10-10.0.10586-SP0
    Current dir: D:\code\LetsExplorePython\Chapter 10 - Standard library
    Executable: python.exe
    Executable dir: C:\apps\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64
    

Process execution example:


```python
###################################
### TODO ##########################
###################################
###################################
###################################









# import sys
# from subprocess import Popen, PIPE

# # ping
# cmd = 'ping -c 1 '
# # No Windows
# if sys.platform == 'win32':
#     cmd = 'ping -n 1 '

# # Local just for testing
# host = '127.0.0.1'

# # Comunicates with another process
# # a pipe with the command stdout
# py = Popen(cmd + host, stdout=PIPE)

# # Shows command output
# print (py.stdout.read())
```

The *subprocess* module provides a generic way of running processes with Popen() function which allows communication with the process through operating system pipes.

Time
-----
Python has two modules to handle time:

+ *Time*: implements functions that allow using the time generated by the system.
+ *Datetime*: implements high-level types to perform date and time operations.

Example with time:


```python
import time

# localtime() Returns a date and local time in the form 
# of a structure called struct_time, which is a 
# collection with the items: year, month, day, hour, minute,
# secund, day of the week, day of the year and e daylight saving time
print (time.localtime())

# asctime() returns a date and hour with string, according to
# operating system configuration
print (time.asctime())

# time() returns system time in seconds
ts1 = time.time()

# gmtime() converts seconds to struct_time
tt1 = time.gmtime(ts1)
print (ts1, '->', tt1)

# Adding an hour
tt2 = time.gmtime(ts1 + 3600)

# mktime() converts struct_time  to seconds
ts2 = time.mktime(tt2)
print (ts2, '->', tt2)

# clock() returs time since the program started, in seconds
print ('The program took', time.clock(), \
    'seconds up to now...')

# Counting seconds...
for i in range(5):
    # sleep() waits the number of seconds specified as parameter
    time.sleep(1)
    print (i + 1, 'second(s)')
```

    time.struct_time(tm_year=2017, tm_mon=4, tm_mday=17, tm_hour=8, tm_min=35, tm_sec=29, tm_wday=0, tm_yday=107, tm_isdst=0)
    Mon Apr 17 08:35:29 2017
    1492398329.4567747 -> time.struct_time(tm_year=2017, tm_mon=4, tm_mday=17, tm_hour=3, tm_min=5, tm_sec=29, tm_wday=0, tm_yday=107, tm_isdst=0)
    1492382129.0 -> time.struct_time(tm_year=2017, tm_mon=4, tm_mday=17, tm_hour=4, tm_min=5, tm_sec=29, tm_wday=0, tm_yday=107, tm_isdst=0)
    The program took 28.407318756660686 seconds up to now...
    1 second(s)
    2 second(s)
    3 second(s)
    4 second(s)
    5 second(s)
    


```python
def countdown(x):
    # Counting seconds...
    for i in range(x):
        # sleep() waits the number of seconds specified as parameter
        time.sleep(1)
        print (i + 1, 'second(s)')

countdown(4)
print("countdown completed")
```

    1 second(s)
    2 second(s)
    3 second(s)
    4 second(s)
    countdown completed
    

In *datetime*, four types are defined for representing time:

+ *datetime*: date and time.
+ *date*: just date.
+ *time*: just time.
+ *timedelta*: time diference.

Example:


```python
import datetime

# datetime() receives as parameter:
# year, month, day, hour, minute, second and 
# returns an object of type datetime
dt = datetime.datetime(2020, 12, 31, 23, 59, 59)

# Objects date and time can be created from
# a datetime object
date = dt.date()
hour = dt.time()

# How many time to 12/31/2020
dd = dt - dt.today()

print ('Date:', date)
print ('Hour:', hour)
print ('How many time to 12/31/2020:', dd)

```

    Date: 2020-12-31
    Hour: 23:59:59
    How many time to 12/31/2020: 1354 days, 15:22:27.025924
    


```python

```

### textwrap — Text wrapping and filling

The `textwrap` module provides some convenience functions, as well as `TextWrapper`, the class that does all the work. If you’re just wrapping or filling one or two text strings, the convenience functions should be good enough; otherwise, you should use an instance of `TextWrapper` for efficiency

* **textwrap.wrap** - Wraps the single paragraph in text (a string) so every line is at most width characters long. Returns a list of output lines, without final newlines. Optional keyword arguments correspond to the instance attributes of TextWrapper, documented below. width defaults to 70.


```python
import textwrap
txt = "    The   `textwrap` module provides some convenience functions, as well as `TextWrapper`, the class that does all the work. If you’re just wrapping or filling one or two text strings, the convenience functions should be good enough; otherwise, you should use an instance of `TextWrapper` for efficiency"
print(txt)

for t in textwrap.wrap(txt):
    print(t)
    
for t in textwrap.wrap(txt, width=100):
    print(t)
    
for t in textwrap.wrap(txt, width=60, initial_indent="* "):
    print(t)
```

        The   `textwrap` module provides some convenience functions, as well as `TextWrapper`, the class that does all the work. If you’re just wrapping or filling one or two text strings, the convenience functions should be good enough; otherwise, you should use an instance of `TextWrapper` for efficiency
        The   `textwrap` module provides some convenience functions, as
    well as `TextWrapper`, the class that does all the work. If you’re
    just wrapping or filling one or two text strings, the convenience
    functions should be good enough; otherwise, you should use an instance
    of `TextWrapper` for efficiency
        The   `textwrap` module provides some convenience functions, as well as `TextWrapper`, the class
    that does all the work. If you’re just wrapping or filling one or two text strings, the convenience
    functions should be good enough; otherwise, you should use an instance of `TextWrapper` for
    efficiency
    *     The   `textwrap` module provides some convenience
    functions, as well as `TextWrapper`, the class that does all
    the work. If you’re just wrapping or filling one or two text
    strings, the convenience functions should be good enough;
    otherwise, you should use an instance of `TextWrapper` for
    efficiency
    

* **textwrap.fill** - Wraps the single paragraph in text, and returns a single string containing the wrapped paragraph. fill() is shorthand for


```python
print(textwrap.fill(txt))
```

        The   `textwrap` module provides some convenience functions, as
    well as `TextWrapper`, the class that does all the work. If you’re
    just wrapping or filling one or two text strings, the convenience
    functions should be good enough; otherwise, you should use an instance
    of `TextWrapper` for efficiency
    

* **textwrap.shorten** - Collapse and truncate the given text to fit in the given width. First the whitespace in text is collapsed (all whitespace is replaced by single spaces). If the result fits in the width, it is returned. Otherwise, enough words are dropped from the end so that the remaining words plus the placeholder fit within width


```python
print(textwrap.shorten(txt, width=60))
print(textwrap.shorten(txt, width=50))
s = textwrap.shorten(txt, width=25, placeholder="...")
print(s)
print(len(s))
s = textwrap.shorten(txt, width=20, placeholder="...")
print(s)
print(len(s))
```

    The `textwrap` module provides some convenience [...]
    The `textwrap` module provides some [...]
    The `textwrap` module...
    24
    The `textwrap`...
    17
    

* **textwrap.dedent** - Remove any common leading whitespace from every line in text.


```python
textwrap.dedent(txt)
```




    'The   `textwrap` module provides some convenience functions, as well as `TextWrapper`, the class that does all the work. If you’re just wrapping or filling one or two text strings, the convenience functions should be good enough; otherwise, you should use an instance of `TextWrapper` for efficiency'



* **textwrap.indent** - Add prefix to the beginning of selected lines in text.


```python
print(textwrap.indent(txt.strip().replace(",", '\n'), '$ '))
```

    $ The   `textwrap` module provides some convenience functions
    $  as well as `TextWrapper`
    $  the class that does all the work. If you’re just wrapping or filling one or two text strings
    $  the convenience functions should be good enough; otherwise
    $  you should use an instance of `TextWrapper` for efficiency
    

## Excersise - Files I/O


1. Write a Python program to read an entire text file.     

2. Write a Python program to read first n lines of a file.     

3. Write a Python program to append text to a file and display the text.     

4. Write a Python program to read last n lines of a file.     

5. Write a Python program to read a file line by line and store it into a list.     

6. Write a Python program to read a file line by line store it into a variable.     

7. Write a Python program to read a file line by line store it into an array.     

8. Write a python program to find the longest words.     

9. Write a Python program to count the number of lines in a text file.     

10. Write a Python program to count the frequency of words in a file.     

11. Write a Python program to get the file size of a plain file.     

12. Write a Python program to write a list to a file.     

13. Write a Python program to copy the contents of a file to another file .     

14. Write a Python program to combine each line from first file with the corresponding line in second file.     

15. Write a Python program to read a random line from a file.     

16. Write a Python program to assess if a file is closed or not.     

17. Write a Python program to remove newline characters from a file.     

## Excersise - OS, zip, csv

* Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.
* Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree.
* Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.
* Create a csv file and traverse it using `csv` module

## Excersise - textwrap

**Pre**: Store entire text of "Excersise - OS, zip, csv" in a string (exc)

1. Print the `exc` with one line spacing
2. Print summary of the `exc` so that only 50 chars are shown
3. Print `exc` in such a manner that it replaces starting "*" with 'Question auto_number:'.


## Excersise - Time

* Write a fuction which can find the time of execution duration of each excercise in sec & also in min. 
* Write a clock which can return the time in multiple timezones.
