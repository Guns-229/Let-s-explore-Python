
Chapter 13: Exceptions
=============================
_____________________________
When a failure occurs in the program (such as division by zero, etc) at runtime, an exception is generated. If the exception is not handled, it will be propagated through function calls to the main program module, interrupting execution.


```python
print(10/0)
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-1-fe01563e1bc6> in <module>
    ----> 1 print(10/0)
    

    ZeroDivisionError: division by zero


The *try* instruction allows exception handling in Python. If an exception occurs in a block marked by *try*, it is possible to handle the exception through the instruction *except*. It is possible to have many *except* blocks for the same *try* block.


```python
try:
    print (1/0)
except ZeroDivisionError as zde:
    print('Error:', zde)
```

    Error: division by zero



```python
try:
    print (1/0)
except Exception as e:
    print ('Error:', e)
```

    Error: division by zero


```python
try:
    raise Exception
    print (1/0)
except ZeroDivisionError:
    print ('Error trying to divide by zero.')
    
```
**Output:**
```
---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
<ipython-input-6-39351026b008> in <module>
      1 try:
----> 2     raise Exception
      3     print (1/0)
      4 except ZeroDivisionError:
      5     print ('Error trying to divide by zero.')

Exception: 
    ```

> **NOTE**
><hr>
> If *except* receives the name of an exception, only that exception will be handled. If no exception name is passed as a parameter, all exceptions will be handled.


```python
import sys

try:
    print("... TESTing.. ")
    with open('myfile.txt', "w") as myFile:
        for a in ["a", "b", "c"]:
            myFile.write(a)
#         for a in ["1", "2", "3", "4", "5", 6]:
        for a in ["1", "2", "3", "4", "5", "6"]:
            myFile.write(a)
    raise ValueError("Test Exception")
    raise NotImplemented("Sorry the code is still missing,\nas developer is taking a break...")
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError as ve:
    print("Could not convert data to an integer.", ve)
    print("Raise the old exception again, and exiting out..")
#     raise   # Reraising the exception.
except:
    print("Unexpected error:", sys.exc_info())
```

    ... TESTing.. 
    Could not convert data to an integer. Test Exception
    Raise the old exception again, and exiting out..



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-13-cb10782f2709> in <module>
          9         for a in ["1", "2", "3", "4", "5", "6"]:
         10             myFile.write(a)
    ---> 11     raise ValueError("Test Exception")
         12     raise NotImplemented("Sorry the code is still missing,\nas developer is taking a break...")
         13 except OSError as err:


    ValueError: Test Exception



```python
# Multiple types of exceptions in single "except"
import sys

try:
    a = "Ja"
#     print(1 > z)
    print(1 / a)
except (OSError, NameError, ValueError, ZeroDivisionError) as err:
    print("Some common error: {0}".format(err))
except TypeError:
    print("Unexpected TypeError error:", sys.exc_info())
```

    Unexpected TypeError error: (<class 'TypeError'>, TypeError("unsupported operand type(s) for /: 'int' and 'str'"), <traceback object at 0x1032e70f0>)



```python
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 08:50:42 2016

@author: mayankjohri@gmail.com
"""
import traceback

# Try to get a file name
try:
#     fn = input('File Name (temp.txt): ').strip()
    fn = "temp.txt"
    # Numbering lines
    for i, s in enumerate(open(fn)):
        print( i + 1,"> ", s,)
        if i == 2:
            raise ValueError("Custom Error Message")
# If an error happens
except Exception as e:
    trace = traceback.format_exc()
    # Show it on the screen
    print ('An error happened:\n', trace)
    # And save it on a file 
    with open("trace_asd.log", "a") as file:
        file.write(trace)
        file.write(f"Error Message: {e}")
```

    1 >  asdf
    
    2 >  asdfdfa
    
    3 >  sas
    
    An error happened:
     Traceback (most recent call last):
      File "<ipython-input-21-948fe50a4b22>", line 17, in <module>
        raise ValueError("Custom Error Message")
    ValueError: Custom Error Message
    



```python
# -*- coding: utf-8 -*-
"""
Saving to log using print_exc

@author: mayankjohri@gmail.com
"""
import traceback

# Try to get a file name
try:
#     fn = input('File Name (temp.txt): ').strip()
    fn = "temp.txt"
    # Numbering lines
    for i, s in enumerate(open(fn)):
        print( i + 1,"> ", s,)
        if i == 2:
            raise ValueError
    
# If an error happens
except:
    # And save it on a file 
    with open("trace_asd.log", "a") as file:
        traceback.print_exc(file=file)
```

    1 >  asdf
    
    2 >  asdfdfa
    
    3 >  sas
    


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

def rollback(e):
    print("reverting the changes as following exception happend")
    print("\t", e)

def commit():
    print("commiting the changes")
    
print("Testing")

try:
#     do_some_stuff()
    do_some_stuff_e()
except Exception as e:
    // add some code for tracelog also.
    rollback(e)
else:
    commit()
finally:
    print("Exiting out")
```

    Testing
    Doing some stuff and will now raise error
    reverting the changes as following exception happend
    	 A very specific bad thing happened
    Exiting out



```python
# Execution Flow
# ----------------
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

## Writing Exception Classes


```python
class HostNotFound(Exception):
    def __init__( self, host):
        self.host = host
        Exception.__init__(self, 'Host Not Found exception: missing %s' % host)

try:
    raise HostNotFound("gitpub.com")
except HostNotFound as hcf:
    # Handle exception.
    print (hcf)  # -> 'Host Not Found exception: missing taoriver.net'
    print (hcf.host)  # -> 'gitpub.com'
```

    Host Not Found exception: missing gitpub.com
    gitpub.com


> **Note:**
> ___
> Normally its not recommended to create your own exception class


```python
try:
    fh = open("nonexisting.txt", "r")
    try:
        fh.write("This is my test file for exception handling!!")
        print(1/0)
    except:
        print("Caught error message")
    finally:
        print ("Going to close the file")
        fh.close()
except IOError:
   print ("Error: can\'t find file or read data")
```

    Error: can't find file or read data



```python
try:
#     fh = open("nonexisting.txt", "r")
    try:
        fh.write("This is my test file for exception handling!!")
        print(1/0)
    except:
        print("Caught error message")
        raise
    finally:
        print ("Going to close the file")
        fh.close()
except:
    print ("Error: can\'t find file or read data")
```

    Caught error message
    Going to close the file
    Error: can't find file or read data



```python
try:
#     fh = open("nonexisting.txt", "r")
    try:
#         fh.write("This is my test file for exception handling!!")
        print(1/0)
    except:
        print("Caught error message") 
    finally:
        print ("Going to close the file")
#         fh.close()print(1/0)
    print(1/0)
except :
    print ("Error: can\'t find file or read data")
    raise
```

    Caught error message
    Going to close the file
    Error: can't find file or read data



    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-33-b22e4735bef5> in <module>()
          9         print ("Going to close the file")
         10 #         fh.close()print(1/0)
    ---> 11     print(1/0)
         12 except :
         13     print ("Error: can\'t find file or read data")


    ZeroDivisionError: integer division or modulo by zero



```python
# Valid construct, but why you will use it. :(

try:
    print("Hello")
finally:
    print("In Finally")
```

    Hello
    In Finally


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
import inspect
inspect.getclasstree(inspect.getmro(Exception))
```




    [(object, ()), [(BaseException, (object,)), [(Exception, (BaseException,))]]]




```python

```

    Help on module inspect:
    
    NAME
        inspect - Get useful information from live Python objects.
    
    DESCRIPTION
        This module encapsulates the interface provided by the internal special
        attributes (co_*, im_*, tb_*, etc.) in a friendlier fashion.
        It also provides some help for examining source code and class layout.
        
        Here are some of the useful functions provided by this module:
        
            ismodule(), isclass(), ismethod(), isfunction(), isgeneratorfunction(),
                isgenerator(), istraceback(), isframe(), iscode(), isbuiltin(),
                isroutine() - check object types
            getmembers() - get members of an object that satisfy a given condition
        
            getfile(), getsourcefile(), getsource() - find an object's source code
            getdoc(), getcomments() - get documentation on an object
            getmodule() - determine the module that an object came from
            getclasstree() - arrange classes so as to represent their hierarchy
        
            getargspec(), getargvalues(), getcallargs() - get info about function arguments
            getfullargspec() - same, with support for Python-3000 features
            formatargspec(), formatargvalues() - format an argument spec
            getouterframes(), getinnerframes() - get info about frames
            currentframe() - get the current stack frame
            stack(), trace() - get info about frames on the stack or in a traceback
        
            signature() - get a Signature object for the callable
    
    CLASSES
        builtins.Exception(builtins.BaseException)
            EndOfBlock
        builtins.object
            BlockFinder
            BoundArguments
            Parameter
            Signature
        builtins.tuple(builtins.object)
            ArgInfo
            ArgSpec
            Arguments
            Attribute
            ClosureVars
            FullArgSpec
            ModuleInfo
            Traceback
        
        class ArgInfo(builtins.tuple)
         |  ArgInfo(args, varargs, keywords, locals)
         |  
         |  Method resolution order:
         |      ArgInfo
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __getnewargs__(self)
         |      Return self as a plain tuple.  Used by copy and pickle.
         |  
         |  __repr__(self)
         |      Return a nicely formatted representation string
         |  
         |  _asdict(self)
         |      Return a new OrderedDict which maps field names to their values.
         |  
         |  _replace(_self, **kwds)
         |      Return a new ArgInfo object replacing specified fields with new values
         |  
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |  
         |  _make(iterable, new=<built-in method __new__ of type object at 0x7f021d0de700>, len=<built-in function len>) from builtins.type
         |      Make a new ArgInfo object from a sequence or iterable
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(_cls, args, varargs, keywords, locals)
         |      Create new instance of ArgInfo(args, varargs, keywords, locals)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  args
         |      Alias for field number 0
         |  
         |  keywords
         |      Alias for field number 2
         |  
         |  locals
         |      Alias for field number 3
         |  
         |  varargs
         |      Alias for field number 1
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  _fields = ('args', 'varargs', 'keywords', 'locals')
         |  
         |  _source = "from builtins import property as _property, tupl..._itemget...
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.n
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return self*value.
         |  
         |  count(...)
         |      T.count(value) -> integer -- return number of occurrences of value
         |  
         |  index(...)
         |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
         |      Raises ValueError if the value is not present.
        
        class ArgSpec(builtins.tuple)
         |  ArgSpec(args, varargs, keywords, defaults)
         |  
         |  Method resolution order:
         |      ArgSpec
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __getnewargs__(self)
         |      Return self as a plain tuple.  Used by copy and pickle.
         |  
         |  __repr__(self)
         |      Return a nicely formatted representation string
         |  
         |  _asdict(self)
         |      Return a new OrderedDict which maps field names to their values.
         |  
         |  _replace(_self, **kwds)
         |      Return a new ArgSpec object replacing specified fields with new values
         |  
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |  
         |  _make(iterable, new=<built-in method __new__ of type object at 0x7f021d0de700>, len=<built-in function len>) from builtins.type
         |      Make a new ArgSpec object from a sequence or iterable
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(_cls, args, varargs, keywords, defaults)
         |      Create new instance of ArgSpec(args, varargs, keywords, defaults)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  args
         |      Alias for field number 0
         |  
         |  defaults
         |      Alias for field number 3
         |  
         |  keywords
         |      Alias for field number 2
         |  
         |  varargs
         |      Alias for field number 1
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  _fields = ('args', 'varargs', 'keywords', 'defaults')
         |  
         |  _source = "from builtins import property as _property, tupl..._itemget...
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.n
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return self*value.
         |  
         |  count(...)
         |      T.count(value) -> integer -- return number of occurrences of value
         |  
         |  index(...)
         |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
         |      Raises ValueError if the value is not present.
        
        class Arguments(builtins.tuple)
         |  Arguments(args, varargs, varkw)
         |  
         |  Method resolution order:
         |      Arguments
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __getnewargs__(self)
         |      Return self as a plain tuple.  Used by copy and pickle.
         |  
         |  __repr__(self)
         |      Return a nicely formatted representation string
         |  
         |  _asdict(self)
         |      Return a new OrderedDict which maps field names to their values.
         |  
         |  _replace(_self, **kwds)
         |      Return a new Arguments object replacing specified fields with new values
         |  
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |  
         |  _make(iterable, new=<built-in method __new__ of type object at 0x7f021d0de700>, len=<built-in function len>) from builtins.type
         |      Make a new Arguments object from a sequence or iterable
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(_cls, args, varargs, varkw)
         |      Create new instance of Arguments(args, varargs, varkw)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  args
         |      Alias for field number 0
         |  
         |  varargs
         |      Alias for field number 1
         |  
         |  varkw
         |      Alias for field number 2
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  _fields = ('args', 'varargs', 'varkw')
         |  
         |  _source = "from builtins import property as _property, tupl..._itemget...
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.n
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return self*value.
         |  
         |  count(...)
         |      T.count(value) -> integer -- return number of occurrences of value
         |  
         |  index(...)
         |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
         |      Raises ValueError if the value is not present.
        
        class Attribute(builtins.tuple)
         |  Attribute(name, kind, defining_class, object)
         |  
         |  Method resolution order:
         |      Attribute
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __getnewargs__(self)
         |      Return self as a plain tuple.  Used by copy and pickle.
         |  
         |  __repr__(self)
         |      Return a nicely formatted representation string
         |  
         |  _asdict(self)
         |      Return a new OrderedDict which maps field names to their values.
         |  
         |  _replace(_self, **kwds)
         |      Return a new Attribute object replacing specified fields with new values
         |  
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |  
         |  _make(iterable, new=<built-in method __new__ of type object at 0x7f021d0de700>, len=<built-in function len>) from builtins.type
         |      Make a new Attribute object from a sequence or iterable
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(_cls, name, kind, defining_class, object)
         |      Create new instance of Attribute(name, kind, defining_class, object)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  defining_class
         |      Alias for field number 2
         |  
         |  kind
         |      Alias for field number 1
         |  
         |  name
         |      Alias for field number 0
         |  
         |  object
         |      Alias for field number 3
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  _fields = ('name', 'kind', 'defining_class', 'object')
         |  
         |  _source = "from builtins import property as _property, tupl..._itemget...
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.n
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return self*value.
         |  
         |  count(...)
         |      T.count(value) -> integer -- return number of occurrences of value
         |  
         |  index(...)
         |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
         |      Raises ValueError if the value is not present.
        
        class BlockFinder(builtins.object)
         |  Provide a tokeneater() method to detect the end of a code block.
         |  
         |  Methods defined here:
         |  
         |  __init__(self)
         |  
         |  tokeneater(self, type, token, srowcol, erowcol, line)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
        
        class BoundArguments(builtins.object)
         |  Result of `Signature.bind` call.  Holds the mapping of arguments
         |  to the function's parameters.
         |  
         |  Has the following public attributes:
         |  
         |  * arguments : OrderedDict
         |      An ordered mutable mapping of parameters' names to arguments' values.
         |      Does not contain arguments' default values.
         |  * signature : Signature
         |      The Signature object that created this instance.
         |  * args : tuple
         |      Tuple of positional arguments values.
         |  * kwargs : dict
         |      Dict of keyword arguments values.
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, other)
         |  
         |  __init__(self, signature, arguments)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  args
         |  
         |  kwargs
         |  
         |  signature
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __hash__ = None
        
        class ClosureVars(builtins.tuple)
         |  ClosureVars(nonlocals, globals, builtins, unbound)
         |  
         |  Method resolution order:
         |      ClosureVars
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __getnewargs__(self)
         |      Return self as a plain tuple.  Used by copy and pickle.
         |  
         |  __repr__(self)
         |      Return a nicely formatted representation string
         |  
         |  _asdict(self)
         |      Return a new OrderedDict which maps field names to their values.
         |  
         |  _replace(_self, **kwds)
         |      Return a new ClosureVars object replacing specified fields with new values
         |  
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |  
         |  _make(iterable, new=<built-in method __new__ of type object at 0x7f021d0de700>, len=<built-in function len>) from builtins.type
         |      Make a new ClosureVars object from a sequence or iterable
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(_cls, nonlocals, globals, builtins, unbound)
         |      Create new instance of ClosureVars(nonlocals, globals, builtins, unbound)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  builtins
         |      Alias for field number 2
         |  
         |  globals
         |      Alias for field number 1
         |  
         |  nonlocals
         |      Alias for field number 0
         |  
         |  unbound
         |      Alias for field number 3
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  _fields = ('nonlocals', 'globals', 'builtins', 'unbound')
         |  
         |  _source = "from builtins import property as _property, tupl..._itemget...
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.n
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return self*value.
         |  
         |  count(...)
         |      T.count(value) -> integer -- return number of occurrences of value
         |  
         |  index(...)
         |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
         |      Raises ValueError if the value is not present.
        
        class EndOfBlock(builtins.Exception)
         |  Method resolution order:
         |      EndOfBlock
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Data descriptors defined here:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.BaseException:
         |  
         |  __delattr__(self, name, /)
         |      Implement delattr(self, name).
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __reduce__(...)
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __setattr__(self, name, value, /)
         |      Implement setattr(self, name, value).
         |  
         |  __setstate__(...)
         |  
         |  __str__(self, /)
         |      Return str(self).
         |  
         |  with_traceback(...)
         |      Exception.with_traceback(tb) --
         |      set self.__traceback__ to tb and return self.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from builtins.BaseException:
         |  
         |  __cause__
         |      exception cause
         |  
         |  __context__
         |      exception context
         |  
         |  __dict__
         |  
         |  __suppress_context__
         |  
         |  __traceback__
         |  
         |  args
        
        class FullArgSpec(builtins.tuple)
         |  FullArgSpec(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)
         |  
         |  Method resolution order:
         |      FullArgSpec
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __getnewargs__(self)
         |      Return self as a plain tuple.  Used by copy and pickle.
         |  
         |  __repr__(self)
         |      Return a nicely formatted representation string
         |  
         |  _asdict(self)
         |      Return a new OrderedDict which maps field names to their values.
         |  
         |  _replace(_self, **kwds)
         |      Return a new FullArgSpec object replacing specified fields with new values
         |  
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |  
         |  _make(iterable, new=<built-in method __new__ of type object at 0x7f021d0de700>, len=<built-in function len>) from builtins.type
         |      Make a new FullArgSpec object from a sequence or iterable
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(_cls, args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)
         |      Create new instance of FullArgSpec(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  annotations
         |      Alias for field number 6
         |  
         |  args
         |      Alias for field number 0
         |  
         |  defaults
         |      Alias for field number 3
         |  
         |  kwonlyargs
         |      Alias for field number 4
         |  
         |  kwonlydefaults
         |      Alias for field number 5
         |  
         |  varargs
         |      Alias for field number 1
         |  
         |  varkw
         |      Alias for field number 2
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  _fields = ('args', 'varargs', 'varkw', 'defaults', 'kwonlyargs', 'kwon...
         |  
         |  _source = "from builtins import property as _property, tupl..._itemget...
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.n
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return self*value.
         |  
         |  count(...)
         |      T.count(value) -> integer -- return number of occurrences of value
         |  
         |  index(...)
         |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
         |      Raises ValueError if the value is not present.
        
        class ModuleInfo(builtins.tuple)
         |  ModuleInfo(name, suffix, mode, module_type)
         |  
         |  Method resolution order:
         |      ModuleInfo
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __getnewargs__(self)
         |      Return self as a plain tuple.  Used by copy and pickle.
         |  
         |  __repr__(self)
         |      Return a nicely formatted representation string
         |  
         |  _asdict(self)
         |      Return a new OrderedDict which maps field names to their values.
         |  
         |  _replace(_self, **kwds)
         |      Return a new ModuleInfo object replacing specified fields with new values
         |  
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |  
         |  _make(iterable, new=<built-in method __new__ of type object at 0x7f021d0de700>, len=<built-in function len>) from builtins.type
         |      Make a new ModuleInfo object from a sequence or iterable
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(_cls, name, suffix, mode, module_type)
         |      Create new instance of ModuleInfo(name, suffix, mode, module_type)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  mode
         |      Alias for field number 2
         |  
         |  module_type
         |      Alias for field number 3
         |  
         |  name
         |      Alias for field number 0
         |  
         |  suffix
         |      Alias for field number 1
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  _fields = ('name', 'suffix', 'mode', 'module_type')
         |  
         |  _source = "from builtins import property as _property, tupl..._itemget...
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.n
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return self*value.
         |  
         |  count(...)
         |      T.count(value) -> integer -- return number of occurrences of value
         |  
         |  index(...)
         |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
         |      Raises ValueError if the value is not present.
        
        class Parameter(builtins.object)
         |  Represents a parameter in a function signature.
         |  
         |  Has the following public attributes:
         |  
         |  * name : str
         |      The name of the parameter as a string.
         |  * default : object
         |      The default value for the parameter if specified.  If the
         |      parameter has no default value, this attribute is set to
         |      `Parameter.empty`.
         |  * annotation
         |      The annotation for the parameter if specified.  If the
         |      parameter has no annotation, this attribute is set to
         |      `Parameter.empty`.
         |  * kind : str
         |      Describes how argument values are bound to the parameter.
         |      Possible values: `Parameter.POSITIONAL_ONLY`,
         |      `Parameter.POSITIONAL_OR_KEYWORD`, `Parameter.VAR_POSITIONAL`,
         |      `Parameter.KEYWORD_ONLY`, `Parameter.VAR_KEYWORD`.
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, other)
         |  
         |  __init__(self, name, kind, *, default, annotation)
         |  
         |  __repr__(self)
         |  
         |  __str__(self)
         |  
         |  replace(self, *, name=<class 'inspect._void'>, kind=<class 'inspect._void'>, annotation=<class 'inspect._void'>, default=<class 'inspect._void'>)
         |      Creates a customized copy of the Parameter.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  annotation
         |  
         |  default
         |  
         |  kind
         |  
         |  name
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  KEYWORD_ONLY = <_ParameterKind: 'KEYWORD_ONLY'>
         |  
         |  POSITIONAL_ONLY = <_ParameterKind: 'POSITIONAL_ONLY'>
         |  
         |  POSITIONAL_OR_KEYWORD = <_ParameterKind: 'POSITIONAL_OR_KEYWORD'>
         |  
         |  VAR_KEYWORD = <_ParameterKind: 'VAR_KEYWORD'>
         |  
         |  VAR_POSITIONAL = <_ParameterKind: 'VAR_POSITIONAL'>
         |  
         |  __hash__ = None
         |  
         |  empty = <class 'inspect._empty'>
        
        class Signature(builtins.object)
         |  A Signature object represents the overall signature of a function.
         |  It stores a Parameter object for each parameter accepted by the
         |  function, as well as information specific to the function itself.
         |  
         |  A Signature object has the following public attributes and methods:
         |  
         |  * parameters : OrderedDict
         |      An ordered mapping of parameters' names to the corresponding
         |      Parameter objects (keyword-only arguments are in the same order
         |      as listed in `code.co_varnames`).
         |  * return_annotation : object
         |      The annotation for the return type of the function if specified.
         |      If the function has no annotation for its return type, this
         |      attribute is set to `Signature.empty`.
         |  * bind(*args, **kwargs) -> BoundArguments
         |      Creates a mapping from positional and keyword arguments to
         |      parameters.
         |  * bind_partial(*args, **kwargs) -> BoundArguments
         |      Creates a partial mapping from positional and keyword arguments
         |      to parameters (simulating 'functools.partial' behavior.)
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, other)
         |  
         |  __init__(self, parameters=None, *, return_annotation, __validate_parameters__=True)
         |      Constructs Signature from the given list of Parameter
         |      objects and 'return_annotation'.  All arguments are optional.
         |  
         |  __str__(self)
         |  
         |  bind(*args, **kwargs)
         |      Get a BoundArguments object, that maps the passed `args`
         |      and `kwargs` to the function's signature.  Raises `TypeError`
         |      if the passed arguments can not be bound.
         |  
         |  bind_partial(*args, **kwargs)
         |      Get a BoundArguments object, that partially maps the
         |      passed `args` and `kwargs` to the function's signature.
         |      Raises `TypeError` if the passed arguments can not be bound.
         |  
         |  replace(self, *, parameters=<class 'inspect._void'>, return_annotation=<class 'inspect._void'>)
         |      Creates a customized copy of the Signature.
         |      Pass 'parameters' and/or 'return_annotation' arguments
         |      to override them in the new copy.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |  
         |  from_builtin(func) from builtins.type
         |  
         |  from_function(func) from builtins.type
         |      Constructs Signature for the given python function
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  parameters
         |  
         |  return_annotation
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __hash__ = None
         |  
         |  empty = <class 'inspect._empty'>
        
        class Traceback(builtins.tuple)
         |  Traceback(filename, lineno, function, code_context, index)
         |  
         |  Method resolution order:
         |      Traceback
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __getnewargs__(self)
         |      Return self as a plain tuple.  Used by copy and pickle.
         |  
         |  __repr__(self)
         |      Return a nicely formatted representation string
         |  
         |  _asdict(self)
         |      Return a new OrderedDict which maps field names to their values.
         |  
         |  _replace(_self, **kwds)
         |      Return a new Traceback object replacing specified fields with new values
         |  
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |  
         |  _make(iterable, new=<built-in method __new__ of type object at 0x7f021d0de700>, len=<built-in function len>) from builtins.type
         |      Make a new Traceback object from a sequence or iterable
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(_cls, filename, lineno, function, code_context, index)
         |      Create new instance of Traceback(filename, lineno, function, code_context, index)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  code_context
         |      Alias for field number 3
         |  
         |  filename
         |      Alias for field number 0
         |  
         |  function
         |      Alias for field number 2
         |  
         |  index
         |      Alias for field number 4
         |  
         |  lineno
         |      Alias for field number 1
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  _fields = ('filename', 'lineno', 'function', 'code_context', 'index')
         |  
         |  _source = "from builtins import property as _property, tupl..._itemget...
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.n
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return self*value.
         |  
         |  count(...)
         |      T.count(value) -> integer -- return number of occurrences of value
    
    FUNCTIONS
        classify_class_attrs(cls)
            Return list of attribute-descriptor tuples.
            
            For each name in dir(cls), the return list contains a 4-tuple
            with these elements:
            
                0. The name (a string).
            
                1. The kind of attribute this is, one of these strings:
                       'class method'    created via classmethod()
                       'static method'   created via staticmethod()
                       'property'        created via property()
                       'method'          any other flavor of method or descriptor
                       'data'            not a method
            
                2. The class which defined this attribute (a class).
            
                3. The object as obtained by calling getattr; if this fails, or if the
                   resulting object does not live anywhere in the class' mro (including
                   metaclasses) then the object is looked up in the defining class's
                   dict (found by walking the mro).
            
            If one of the items in dir(cls) is stored in the metaclass it will now
            be discovered and not have None be listed as the class in which it was
            defined.  Any items whose home class cannot be discovered are skipped.
        
        cleandoc(doc)
            Clean up indentation from docstrings.
            
            Any whitespace that can be uniformly removed from the second line
            onwards is removed.
        
        currentframe()
            Return the frame of the caller or None if this is not possible.
        
        findsource(object)
            Return the entire source file and starting line number for an object.
            
            The argument may be a module, class, method, function, traceback, frame,
            or code object.  The source code is returned as a list of all the lines
            in the file and the line number indexes a line in that list.  An OSError
            is raised if the source code cannot be retrieved.
        
        formatannotation(annotation, base_module=None)
        
        formatannotationrelativeto(object)
        
        formatargspec(args, varargs=None, varkw=None, defaults=None, kwonlyargs=(), kwonlydefaults={}, annotations={}, formatarg=<class 'str'>, formatvarargs=<function <lambda> at 0x7f021a7e6598>, formatvarkw=<function <lambda> at 0x7f021a7e6620>, formatvalue=<function <lambda> at 0x7f021a7e66a8>, formatreturns=<function <lambda> at 0x7f021a7e6730>, formatannotation=<function formatannotation at 0x7f021a7e6488>)
            Format an argument spec from the values returned by getargspec
            or getfullargspec.
            
            The first seven arguments are (args, varargs, varkw, defaults,
            kwonlyargs, kwonlydefaults, annotations).  The other five arguments
            are the corresponding optional formatting functions that are called to
            turn names and values into strings.  The last argument is an optional
            function to format the sequence of arguments.
        
        formatargvalues(args, varargs, varkw, locals, formatarg=<class 'str'>, formatvarargs=<function <lambda> at 0x7f021a7e6840>, formatvarkw=<function <lambda> at 0x7f021a7e68c8>, formatvalue=<function <lambda> at 0x7f021a7e6950>)
            Format an argument spec from the 4 values returned by getargvalues.
            
            The first four arguments are (args, varargs, varkw, locals).  The
            next four arguments are the corresponding optional formatting functions
            that are called to turn names and values into strings.  The ninth
            argument is an optional function to format the sequence of arguments.
        
        getabsfile(object, _filename=None)
            Return an absolute path to the source or compiled file for an object.
            
            The idea is for each object to have a unique origin, so this routine
            normalizes the result as much as possible.
        
        getargs(co)
            Get information about the arguments accepted by a code object.
            
            Three things are returned: (args, varargs, varkw), where
            'args' is the list of argument names. Keyword-only arguments are
            appended. 'varargs' and 'varkw' are the names of the * and **
            arguments or None.
        
        getargspec(func)
            Get the names and default values of a function's arguments.
            
            A tuple of four things is returned: (args, varargs, varkw, defaults).
            'args' is a list of the argument names.
            'args' will include keyword-only argument names.
            'varargs' and 'varkw' are the names of the * and ** arguments or None.
            'defaults' is an n-tuple of the default values of the last n arguments.
            
            Use the getfullargspec() API for Python-3000 code, as annotations
            and keyword arguments are supported. getargspec() will raise ValueError
            if the func has either annotations or keyword arguments.
        
        getargvalues(frame)
            Get information about arguments passed into a particular frame.
            
            A tuple of four things is returned: (args, varargs, varkw, locals).
            'args' is a list of the argument names.
            'varargs' and 'varkw' are the names of the * and ** arguments or None.
            'locals' is the locals dictionary of the given frame.
        
        getattr_static(obj, attr, default=<object object at 0x7f021bf710b0>)
            Retrieve attributes without triggering dynamic lookup via the
            descriptor protocol,  __getattr__ or __getattribute__.
            
            Note: this function may not be able to retrieve all attributes
            that getattr can fetch (like dynamically created attributes)
            and may find attributes that getattr can't (like descriptors
            that raise AttributeError). It can also return descriptor objects
            instead of instance members in some cases. See the
            documentation for details.
        
        getblock(lines)
            Extract the block of code at the top of the given list of lines.
        
        getcallargs(*func_and_positional, **named)
            Get the mapping of arguments to values.
            
            A dict is returned, with keys the function argument names (including the
            names of the * and ** arguments, if any), and values the respective bound
            values from 'positional' and 'named'.
        
        getclasstree(classes, unique=False)
            Arrange the given list of classes into a hierarchy of nested lists.
            
            Where a nested list appears, it contains classes derived from the class
            whose entry immediately precedes the list.  Each entry is a 2-tuple
            containing a class and a tuple of its base classes.  If the 'unique'
            argument is true, exactly one entry appears in the returned structure
            for each class in the given list.  Otherwise, classes using multiple
            inheritance and their descendants will appear multiple times.
        
        getclosurevars(func)
            Get the mapping of free variables to their current values.
            
            Returns a named tuple of dicts mapping the current nonlocal, global
            and builtin references as seen by the body of the function. A final
            set of unbound names that could not be resolved is also provided.
        
        getcomments(object)
            Get lines of comments immediately preceding an object's source code.
            
            Returns None when source can't be found.
        
        getdoc(object)
            Get the documentation string for an object.
            
            All tabs are expanded to spaces.  To clean up docstrings that are
            indented to line up with blocks of code, any whitespace than can be
            uniformly removed from the second line onwards is removed.
        
        getfile(object)
            Work out which source or compiled file an object was defined in.
        
        getframeinfo(frame, context=1)
            Get information about a frame or traceback object.
            
            A tuple of five things is returned: the filename, the line number of
            the current line, the function name, a list of lines of context from
            the source code, and the index of the current line within that list.
            The optional second argument specifies the number of lines of context
            to return, which are centered around the current line.
        
        getfullargspec(func)
            Get the names and default values of a callable object's arguments.
            
            A tuple of seven things is returned:
            (args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults annotations).
            'args' is a list of the argument names.
            'varargs' and 'varkw' are the names of the * and ** arguments or None.
            'defaults' is an n-tuple of the default values of the last n arguments.
            'kwonlyargs' is a list of keyword-only argument names.
            'kwonlydefaults' is a dictionary mapping names from kwonlyargs to defaults.
            'annotations' is a dictionary mapping argument names to annotations.
            
            The first four items in the tuple correspond to getargspec().
        
        getgeneratorlocals(generator)
            Get the mapping of generator local variables to their current values.
            
            A dict is returned, with the keys the local variable names and values the
            bound values.
        
        getgeneratorstate(generator)
            Get current state of a generator-iterator.
            
            Possible states are:
              GEN_CREATED: Waiting to start execution.
              GEN_RUNNING: Currently being executed by the interpreter.
              GEN_SUSPENDED: Currently suspended at a yield expression.
              GEN_CLOSED: Execution has completed.
        
        getinnerframes(tb, context=1)
            Get a list of records for a traceback's frame and all lower frames.
            
            Each record contains a frame object, filename, line number, function
            name, a list of lines of context, and index within the context.
        
        getlineno(frame)
            Get the line number from a frame object, allowing for optimization.
        
        getmembers(object, predicate=None)
            Return all members of an object as (name, value) pairs sorted by name.
            Optionally, only return members that satisfy a given predicate.
        
        getmodule(object, _filename=None)
            Return the module an object was defined in, or None if not found.
        
        getmoduleinfo(path)
            Get the module name, suffix, mode, and module type for a given file.
        
        getmodulename(path)
            Return the module name for a given file, or None.
        
        getmro(cls)
            Return tuple of base classes (including cls) in method resolution order.
        
        getouterframes(frame, context=1)
            Get a list of records for a frame and all higher (calling) frames.
            
            Each record contains a frame object, filename, line number, function
            name, a list of lines of context, and index within the context.
        
        getsource(object)
            Return the text of the source code for an object.
            
            The argument may be a module, class, method, function, traceback, frame,
            or code object.  The source code is returned as a single string.  An
            OSError is raised if the source code cannot be retrieved.
        
        getsourcefile(object)
            Return the filename that can be used to locate an object's source.
            Return None if no way can be identified to get the source.
        
        getsourcelines(object)
            Return a list of source lines and starting line number for an object.
            
            The argument may be a module, class, method, function, traceback, frame,
            or code object.  The source code is returned as a list of the lines
            corresponding to the object and the line number indicates where in the
            original source file the first line of code was found.  An OSError is
            raised if the source code cannot be retrieved.
        
        indentsize(line)
            Return the indent size, in spaces, at the start of a line of text.
        
        isabstract(object)
            Return true if the object is an abstract base class (ABC).
        
        isbuiltin(object)
            Return true if the object is a built-in function or method.
            
            Built-in functions and methods provide these attributes:
                __doc__         documentation string
                __name__        original name of this function or method
                __self__        instance to which a method is bound, or None
        
        isclass(object)
            Return true if the object is a class.
            
            Class objects provide these attributes:
                __doc__         documentation string
                __module__      name of module in which this class was defined
        
        iscode(object)
            Return true if the object is a code object.
            
            Code objects provide these attributes:
                co_argcount     number of arguments (not including * or ** args)
                co_code         string of raw compiled bytecode
                co_consts       tuple of constants used in the bytecode
                co_filename     name of file in which this code object was created
                co_firstlineno  number of first line in Python source code
                co_flags        bitmap: 1=optimized | 2=newlocals | 4=*arg | 8=**arg
                co_lnotab       encoded mapping of line numbers to bytecode indices
                co_name         name with which this code object was defined
                co_names        tuple of names of local variables
                co_nlocals      number of local variables
                co_stacksize    virtual machine stack space required
                co_varnames     tuple of names of arguments and local variables
        
        isdatadescriptor(object)
            Return true if the object is a data descriptor.
            
            Data descriptors have both a __get__ and a __set__ attribute.  Examples are
            properties (defined in Python) and getsets and members (defined in C).
            Typically, data descriptors will also have __name__ and __doc__ attributes
            (properties, getsets, and members have both of these attributes), but this
            is not guaranteed.
        
        isframe(object)
            Return true if the object is a frame object.
            
            Frame objects provide these attributes:
                f_back          next outer frame object (this frame's caller)
                f_builtins      built-in namespace seen by this frame
                f_code          code object being executed in this frame
                f_globals       global namespace seen by this frame
                f_lasti         index of last attempted instruction in bytecode
                f_lineno        current line number in Python source code
                f_locals        local namespace seen by this frame
                f_trace         tracing function for this frame, or None
        
        isfunction(object)
            Return true if the object is a user-defined function.
            
            Function objects provide these attributes:
                __doc__         documentation string
                __name__        name with which this function was defined
                __code__        code object containing compiled function bytecode
                __defaults__    tuple of any default values for arguments
                __globals__     global namespace in which this function was defined
                __annotations__ dict of parameter annotations
                __kwdefaults__  dict of keyword only parameters with defaults
        
        isgenerator(object)
            Return true if the object is a generator.
            
            Generator objects provide these attributes:
                __iter__        defined to support iteration over container
                close           raises a new GeneratorExit exception inside the
                                generator to terminate the iteration
                gi_code         code object
                gi_frame        frame object or possibly None once the generator has
                                been exhausted
                gi_running      set to 1 when generator is executing, 0 otherwise
                next            return the next item from the container
                send            resumes the generator and "sends" a value that becomes
                                the result of the current yield-expression
                throw           used to raise an exception inside the generator
        
        isgeneratorfunction(object)
            Return true if the object is a user-defined generator function.
            
            Generator function objects provides same attributes as functions.
            
            See help(isfunction) for attributes listing.
        
        isgetsetdescriptor(object)
            Return true if the object is a getset descriptor.
            
            getset descriptors are specialized descriptors defined in extension
            modules.
        
        ismemberdescriptor(object)
            Return true if the object is a member descriptor.
            
            Member descriptors are specialized descriptors defined in extension
            modules.
        
        ismethod(object)
            Return true if the object is an instance method.
            
            Instance method objects provide these attributes:
                __doc__         documentation string
                __name__        name with which this method was defined
                __func__        function object containing implementation of method
                __self__        instance to which this method is bound
        
        ismethoddescriptor(object)
            Return true if the object is a method descriptor.
            
            But not if ismethod() or isclass() or isfunction() are true.
            
            This is new in Python 2.2, and, for example, is true of int.__add__.
            An object passing this test has a __get__ attribute but not a __set__
            attribute, but beyond that the set of attributes varies.  __name__ is
            usually sensible, and __doc__ often is.
            
            Methods implemented via descriptors that also pass one of the other
            tests return false from the ismethoddescriptor() test, simply because
            the other tests promise more -- you can, e.g., count on having the
            __func__ attribute (etc) when an object passes ismethod().
        
        ismodule(object)
            Return true if the object is a module.
            
            Module objects provide these attributes:
                __cached__      pathname to byte compiled file
                __doc__         documentation string
                __file__        filename (missing for built-in modules)
        
        isroutine(object)
            Return true if the object is any kind of function or method.
        
        istraceback(object)
            Return true if the object is a traceback.
            
            Traceback objects provide these attributes:
                tb_frame        frame object at this level
                tb_lasti        index of last attempted instruction in bytecode
                tb_lineno       current line number in Python source code
                tb_next         next inner traceback object (called by this level)
        
        signature(obj)
            Get a signature object for the passed callable.
        
        stack(context=1)
            Return a list of records for the stack above the caller's frame.
        
        trace(context=1)
            Return a list of records for the stack below the current exception.
        
        unwrap(func, *, stop=None)
            Get the object wrapped by *func*.
            
            Follows the chain of :attr:`__wrapped__` attributes returning the last
            object in the chain.
            
            *stop* is an optional callback accepting an object in the wrapper chain
            as its sole argument that allows the unwrapping to be terminated early if
            the callback returns a true value. If the callback never returns a true
            value, the last object in the chain is returned as usual. For example,
            :func:`signature` uses this to stop unwrapping if any object in the
            chain has a ``__signature__`` attribute defined.
            
            :exc:`ValueError` is raised if a cycle is encountered.
        
        walktree(classes, children, parent)
            Recursive helper function for getclasstree().
    
    DATA
        CO_GENERATOR = 32
        CO_NESTED = 16
        CO_NEWLOCALS = 2
        CO_NOFREE = 64
        CO_OPTIMIZED = 1
        CO_VARARGS = 4
        CO_VARKEYWORDS = 8
        GEN_CLOSED = 'GEN_CLOSED'
        GEN_CREATED = 'GEN_CREATED'
        GEN_RUNNING = 'GEN_RUNNING'
        GEN_SUSPENDED = 'GEN_SUSPENDED'
        TPFLAGS_IS_ABSTRACT = 1048576
        k = 64
        mod_dict = {'ArgInfo': <class 'inspect.ArgInfo'>, 'ArgSpec': <class 'i...
        modulesbyfile = {'/home/mayank/.local/lib64/python3.4/site-packages/co...
        v = 'NOFREE'
    
    AUTHOR
        ('Ka-Ping Yee <ping@lfw.org>', 'Yury Selivanov <yselivanov@sprymix.com>')
    
    FILE
        /usr/lib64/python3.4/inspect.py
    
    



```python
# https://stackoverflow.com/questions/18296653/print-the-python-exception-error-hierarchy
def classtree(cls, indent=0):
    print ('.' * indent, cls.__name__)
    for subcls in cls.__subclasses__():
        classtree(subcls, indent + 3)

classtree(BaseException)
```

     BaseException
    ... Exception
    ...... TypeError
    ......... MultipartConversionError
    ......... FloatOperation
    ...... StopIteration
    ...... ExceptionPexpect
    ......... EOF
    ......... TIMEOUT
    ...... error
    ...... _Stop
    ...... NameError
    ......... UnboundLocalError
    ...... TraitError
    ...... TokenError
    ...... QueueFull
    ...... OptionError
    ...... Restart
    ...... UnknownKeyError
    ...... GetoptError
    ...... MemoryError
    ...... LeakedCallbackError
    ...... ReturnValueIgnoredError
    ...... ConfigError
    ......... ConfigLoaderError
    ............ ArgumentError
    ......... ConfigFileNotFound
    ...... LargeZipFile
    ...... TimeoutError
    ...... PtyProcessError
    ...... LimitOverrunError
    ...... error
    ...... StackContextInconsistentError
    ...... NoIPAddresses
    ...... Return
    ...... OSError
    ......... ConnectionError
    ............ BrokenPipeError
    ............ ConnectionAbortedError
    ............ ConnectionRefusedError
    ............ ConnectionResetError
    ......... BlockingIOError
    ......... InterruptedError
    ............ InterruptedSystemCall
    ......... SSLError
    ............ SSLZeroReturnError
    ............ SSLWantReadError
    ............ SSLSyscallError
    ............ SSLWantWriteError
    ............ SSLEOFError
    ......... gaierror
    ......... timeout
    ......... UnsupportedOperation
    ......... SpecialFileError
    ......... ProcessLookupError
    ......... FileNotFoundError
    ......... ReadError
    ......... NotADirectoryError
    ......... herror
    ......... Error
    ............ SameFileError
    ......... ExecError
    ......... ItimerError
    ......... PermissionError
    ......... FileExistsError
    ......... ChildProcessError
    ......... TimeoutError
    ......... IsADirectoryError
    ...... SystemError
    ......... CodecRegistryError
    ...... error
    ...... Warning
    ...... ProfileDirError
    ...... ReturnValueIgnoredError
    ...... ExpatError
    ...... TimeoutError
    ...... RecursiveGrammarException
    ...... HeightIsUnknownError
    ...... Error
    ...... InvalidPortNumber
    ...... AliasError
    ......... InvalidAliasError
    ...... Incomplete
    ...... ImportError
    ......... ZipImportError
    ...... PickleError
    ......... PicklingError
    ......... UnpicklingError
    ...... ResolutionError
    ......... VersionConflict
    ............ ContextualVersionConflict
    ......... DistributionNotFound
    ......... UnknownExtra
    ...... Error
    ......... CancelledError
    ......... TimeoutError
    ......... InvalidStateError
    ...... Error
    ...... EditReadOnlyBuffer
    ...... StopTokenizing
    ...... AttributeError
    ...... KillEmbeded
    ...... LookupError
    ......... IndexError
    ......... KeyError
    ............ UnknownBackend
    ............ NoSuchKernel
    ......... CodecRegistryError
    ...... MessageError
    ......... MessageParseError
    ............ HeaderParseError
    ............ BoundaryError
    ......... MultipartConversionError
    ......... CharsetError
    ...... InputRejected
    ...... error
    ...... Empty
    ...... SyntaxError
    ......... IndentationError
    ............ TabError
    ...... AssertionError
    ...... EOFError
    ......... IncompleteReadError
    ...... SubprocessError
    ......... CalledProcessError
    ......... TimeoutExpired
    ...... QueueEmpty
    ...... OptParseError
    ......... OptionError
    ............ OptionConflictError
    ......... OptionValueError
    ......... BadOptionError
    ............ AmbiguousOptionError
    ...... ErrorDuringImport
    ...... DuplicateKernelError
    ...... BufferError
    ...... ValueError
    ......... UnicodeError
    ............ UnicodeEncodeError
    ............ UnicodeDecodeError
    ............ UnicodeTranslateError
    ......... NetmaskValueError
    ......... ClassNotFound
    ......... IllegalMonthError
    ......... Error
    ......... UndefinedComparison
    ......... CertificateError
    ......... InvalidMarker
    ......... InvalidVersion
    ......... InvalidFileException
    ......... JSONDecodeError
    ......... MessageDefect
    ............ NoBoundaryInMultipartDefect
    ............ HeaderDefect
    ............... InvalidHeaderDefect
    ............... HeaderMissingRequiredValue
    ............... NonPrintableDefect
    ............... ObsoleteHeaderDefect
    ............... NonASCIILocalPartDefect
    ............ InvalidBase64PaddingDefect
    ............ InvalidMultipartContentTransferEncodingDefect
    ............ MisplacedEnvelopeHeaderDefect
    ............ UndecodableBytesDefect
    ............ FirstHeaderLineIsContinuationDefect
    ............ MissingHeaderBodySeparatorDefect
    ............ MultipartInvariantViolationDefect
    ............ StartBoundaryNotFoundDefect
    ............ CloseBoundaryNotFoundDefect
    ............ InvalidBase64CharactersDefect
    ......... InvalidSpecifier
    ......... AddressValueError
    ......... UndefinedEnvironmentName
    ......... IllegalWeekdayError
    ......... ClipboardEmpty
    ......... UnsupportedOperation
    ......... InvalidRequirement
    ......... MacroToEdit
    ......... RequirementParseError
    ...... error
    ...... ParseBaseException
    ......... ParseException
    ......... ParseFatalException
    ............ ParseSyntaxException
    ...... BadYieldError
    ...... IPythonError
    ......... KernelError
    ............ TaskRejectError
    ............ NoEnginesRegistered
    ............ UnmetDependency
    ............... ImpossibleDependency
    .................. DependencyTimeout
    .................. InvalidDependency
    ............ RemoteError
    ............... CompositeError
    ............ TimeoutError
    ............ EngineError
    ............ TaskTimeout
    ............ TaskAborted
    ...... LZMAError
    ...... _OptionError
    ...... ProcessError
    ......... BufferTooShort
    ......... TimeoutError
    ......... AuthenticationError
    ...... ReferenceError
    ...... RuntimeError
    ......... NotImplementedError
    ............ StdinNotImplementedError
    ............ ZMQVersionError
    ......... _DeadlockError
    ......... BrokenProcessPool
    ......... BrokenBarrierError
    ......... ExtractionError
    ...... Error
    ...... InteractivelyDefined
    ...... ArgumentError
    ...... IPythonCoreError
    ......... TryNext
    ......... UsageError
    ......... StdinNotImplementedError
    ...... BdbQuit
    ...... Warning
    ......... UserWarning
    ............ GetPassWarning
    ............ FormatterWarning
    ......... DeprecationWarning
    ............ ProvisionalWarning
    ......... ImportWarning
    ......... UnicodeWarning
    ......... PendingDeprecationWarning
    ......... BytesWarning
    ......... SyntaxWarning
    ......... ResourceWarning
    ......... RuntimeWarning
    ............ PEP440Warning
    ......... FutureWarning
    ...... Error
    ......... InterfaceError
    ......... DatabaseError
    ............ OperationalError
    ............ ProgrammingError
    ............ NotSupportedError
    ............ DataError
    ............ InternalError
    ............ IntegrityError
    ...... SpaceInInput
    ...... FindCmdError
    ...... EndOfBlock
    ...... ZMQBaseError
    ......... ZMQError
    ............ ContextTerminated
    ............ Again
    ............ InterruptedSystemCall
    ......... ZMQBindError
    ......... NotDone
    ...... ArgumentError
    ...... ApplicationError
    ...... PrefilterError
    ...... ArithmeticError
    ......... FloatingPointError
    ......... OverflowError
    ......... DecimalException
    ............ FloatOperation
    ............ Rounded
    ............... Underflow
    ............... Overflow
    ............ Inexact
    ............... Underflow
    ............... Overflow
    ............ DivisionByZero
    ............ Clamped
    ............ Subnormal
    ............... Underflow
    ............ InvalidOperation
    ............... ConversionSyntax
    ............... DivisionImpossible
    ............... DivisionUndefined
    ............... InvalidContext
    ......... ZeroDivisionError
    ............ DivisionByZero
    ............ DivisionUndefined
    ...... Full
    ...... ConfigurableError
    ......... MultipleInstanceError
    ...... StopTokenizing
    ...... RegistryError
    ...... KeyReuseError
    ...... HomeDirError
    ...... ValidationError
    ...... TokenError
    ...... ArgumentTypeError
    ...... BadZipFile
    ...... ErrorToken
    ...... TarError
    ......... ExtractError
    ......... ReadError
    ......... CompressionError
    ......... StreamError
    ......... HeaderError
    ............ EmptyHeaderError
    ............ TruncatedHeaderError
    ............ EOFHeaderError
    ............ SubsequentHeaderError
    ............ InvalidHeaderError
    ... GeneratorExit
    ... KeyboardInterrupt
    ... SystemExit

