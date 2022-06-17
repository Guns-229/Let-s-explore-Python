
Chapter 13: Exceptions
=============================
_____________________________
When a failure occurs in the program (such as division by zero, for example) at runtime, an exception is generated. If the exception is not handled, it will be propagated through function calls to the main program module, interrupting execution.


```python
print (10/0)
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-1-70d9038e7f5b> in <module>()
    ----> 1 print (10/0)
    

    ZeroDivisionError: division by zero


The *try* instruction allows exception handling in Python. If an exception occurs in a block marked by *try*, it is possible to handle the exception through the instruction *except*. It is possible to have many *except* blocks for the same *try* block.


```python
try:
    print (1/0)
except ZeroDivisionError:
    print ('Error trying to divide by zero.')
```

    Error trying to divide by zero.
    

If *except* receives the name of an exception, only that exception will be handled. If no exception name is passed as a parameter, all exceptions will be handled.

Example:


```python
import sys

try:
    print("... TESTing.. ")
    with open('myfile.txt', "w") as myFile:
#         for a in ["a", "b", "c"]:
#             myFile.write(str(a))
        for a in [1,2,3,4,5,6]:
            myFile.write(str(a))

    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
    raise Exception("Test Exception")
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info())
    try:
        print(1/0)
    except:
        print("Hallo, Ja")
    raise
```

    ... TESTing.. 
    Unexpected error: (<class 'Exception'>, Exception('Test Exception',), <traceback object at 0x0000013D63D75D08>)
    Hallo, Ja
    


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-13-af3dab30e3b4> in <module>()
         12     s = f.readline()
         13     i = int(s.strip())
    ---> 14     raise Exception("Test Exception")
         15 except OSError as err:
         16     print("OS error: {0}".format(err))
    

    Exception: Test Exception



```python
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 08:50:42 2016

@author: mayankjohri@gmail.com
"""
import traceback

# Try to get a file name
try:
    fn = input('File Name (temp.txt): ').strip()

    # Numbering lines
    for i, s in enumerate(open(fn)):
        print( i + 1,"> ", s,)

# If an error happens
except:

    # Show it on the screen
    trace = traceback.format_exc()

    # And save it on a file
    print ('An error happened:\n', trace)
 
    with open("trace_asd.log", "a+") as file:
        file.write(trace)
    
#    file('trace_asd.log', 'a').write(trace)

    # end the program
#     raise SystemExit
```

    File Name (temp.txt): sdf
    An error happened:
     Traceback (most recent call last):
      File "<ipython-input-16-8191bac69ded>", line 14, in <module>
        for i, s in enumerate(open(fn)):
    FileNotFoundError: [Errno 2] No such file or directory: 'sdf'
    
    

The module *traceback* offers functions for dealing with error messages. The function format_exc() returns the output of the last exception formatted in a *string*.

The handling of exceptions may have an *else* block, which will be executed when no exception occurs and a *finally* block, which will be executed anyway, whether an exception occurred or <span class="note" title="The finally declaration may be used for freeing resources that were used in the try block, such as database connections or open files.">not</span>. New types of exceptions may be defined through inheritance of the class *Exception*.

Since version 2.6, the instruction *with* is available, that may replace the combination of *try / finally* in many situations. It is possible to define an object that will be used during the *with* block execution. The object will support the context management protocol, which means that it will need to have an `__enter__()` method, which will be executed at the beginning of the block, and another called `__exit__()`, which will be called at the end of the block.

Example:


```python
def do_some_stuff():
    print("Doing some stuff")

def do_some_stuff_e():
    print("Doing some stuff and will now raise error")
    raise ValueError('A very specific bad thing happened')

def rollback():
    print("reverting the changes")

def commit():
    print("commiting the changes")
    
print("Testing")

try:
  do_some_stuff()
#   do_some_stuff_e()
except:
  rollback()
#   raise 
else:
  commit()
finally:
    print("Exiting out")
    
# #### ERROR Condtion
# Testing
#     try block
# Doing some stuff and will now raise error
#     except block
# reverting the changes
#     Finally block
# Exiting out

# NO ERROR
# Testing
#     Try block
# Doing some stuff
#     else block
# commiting the changes
#     finally block
# Exiting out


```


      File "<ipython-input-22-11b4c309656a>", line 40
        else block
           ^
    SyntaxError: invalid syntax
    


## Writing Exception Classes
---


```python
class HostNotFound(Exception):
    def __init__( self, host ):
        self.host = host
        Exception.__init__(self, 'Host Not Found exception: missing %s' % host)

try:
    raise HostNotFound("taoriver.net")
except HostNotFound as exc:
    # Handle exception.
    print (exc)  # -> 'Host Not Found exception: missing taoriver.net'
    print (exc.host)  # -> 'taoriver.net'
```

    Host Not Found exception: missing taoriver.net
    taoriver.net
    


```python
try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
        print(1/0)
    except:
        print("Caught erorr message")
    finally:
        print ("Going to close the file")
        fh.close()
except IOError:
   print ("Error: can\'t find file or read data")
```

    Caught erorr message
    Going to close the file
    

## Exception hierarchy

The class hierarchy for built-in exceptions is:

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning

```


```python

```




<style>
    @font-face {
        font-family: "Computer Modern";
        src: url('http://mirrors.ctan.org/fonts/cm-unicode/fonts/otf/cmunss.otf');
    }
    div.cell{
        width:800px;
        margin-left:16% !important;
        margin-right:auto;
    }
    h1 {
        font-family: Helvetica, serif;
    }
    h4{
        margin-top:12px;
        margin-bottom: 3px;
       }
    div.text_cell_render{
        font-family: Computer Modern, "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;
        line-height: 145%;
        font-size: 130%;
        width:800px;
        margin-left:auto;
        margin-right:auto;
    }
    .CodeMirror{
            font-family: "Source Code Pro", source-code-pro,Consolas, monospace;
    }
    .note{
            border-bottom: 1px black dotted;
    }
    .prompt{
        display: None;
    }
    .text_cell_render h5 {
        font-weight: 300;
        font-size: 16pt;
        color: #4057A1;
        font-style: italic;
        margin-bottom: .5em;
        margin-top: 0.5em;
        display: block;
    }
    
    .warning{
        color: rgb( 240, 20, 20 )
        }  
</style>
<script>
    MathJax.Hub.Config({
                        TeX: {
                           extensions: ["AMSmath.js"]
                           },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
                },
                displayAlign: 'center', // Change this to 'center' to center equations.
                "HTML-CSS": {
                    styles: {'.MathJax_Display': {"margin": 4}}
                }
        });
</script>


