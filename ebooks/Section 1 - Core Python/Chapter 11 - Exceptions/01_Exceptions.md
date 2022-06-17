
Chapter 13: Exceptions
=============================
_____________________________
When a failure occurs in the program (such as division by zero, etc) at runtime, an exception is generated. If the exception is not handled, it will be propagated through function calls to the main program module, interrupting execution.

```python
print(10/0)
```

**Output:**
```python
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-1-fe01563e1bc6> in <module>
----> 1 print(10/0)

ZeroDivisionError: division by zero
    ```

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

    Unexpected TypeError error: (<class 'TypeError'>, TypeError("unsupported operand type(s) for /: 'int' and 'str'"), <traceback object at 0x106f6e640>)



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
      File "<ipython-input-5-948fe50a4b22>", line 17, in <module>
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
    # add some code for tracelog also.
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
    try:
        print(1/0)
    except:
        print("Caught error message") 
    finally:
        print ("Going to close the file")
    print(1/0)
except :
    print ("Error: can\'t find file or read data")
    raise
```
**Output:**
```python
Caught error message
Going to close the file
Error: can't find file or read data
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-12-5286be6ebe6e> in <module>
      9         print ("Going to close the file")
     10 #         fh.close()print(1/0)
---> 11     print(1/0)
     12 except :
     13     print ("Error: can\'t find file or read data")

ZeroDivisionError: division by zero
```


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
    ...... StopAsyncIteration
    ...... StopIteration
    ...... ImportError
    ......... ModuleNotFoundError
    ......... ZipImportError
    ...... OSError
    ......... ConnectionError
    ............ BrokenPipeError
    ............ ConnectionAbortedError
    ............ ConnectionRefusedError
    ............ ConnectionResetError
    ............... RemoteDisconnected
    ......... BlockingIOError
    ......... ChildProcessError
    ......... FileExistsError
    ......... FileNotFoundError
    ......... IsADirectoryError
    ......... NotADirectoryError
    ......... InterruptedError
    ............ InterruptedSystemCall
    ......... PermissionError
    ......... ProcessLookupError
    ......... TimeoutError
    ......... UnsupportedOperation
    ......... ItimerError
    ......... Error
    ............ SameFileError
    ......... SpecialFileError
    ......... ExecError
    ......... ReadError
    ......... herror
    ......... gaierror
    ......... timeout
    ......... SSLError
    ............ SSLCertVerificationError
    ............ SSLZeroReturnError
    ............ SSLWantReadError
    ............ SSLWantWriteError
    ............ SSLSyscallError
    ............ SSLEOFError
    ......... URLError
    ............ HTTPError
    ............ ContentTooShortError
    ...... EOFError
    ......... IncompleteReadError
    ...... RuntimeError
    ......... RecursionError
    ......... NotImplementedError
    ............ StdinNotImplementedError
    ............ ZMQVersionError
    ......... _DeadlockError
    ......... BrokenBarrierError
    ......... BrokenExecutor
    ......... SendfileNotAvailableError
    ...... NameError
    ......... UnboundLocalError
    ...... AttributeError
    ...... SyntaxError
    ......... IndentationError
    ............ TabError
    ...... LookupError
    ......... IndexError
    ......... KeyError
    ............ UnknownBackend
    ............ NoSuchKernel
    ......... CodecRegistryError
    ...... ValueError
    ......... UnicodeError
    ............ UnicodeEncodeError
    ............ UnicodeDecodeError
    ............ UnicodeTranslateError
    ......... UnsupportedOperation
    ......... JSONDecodeError
    ......... ClassNotFound
    ......... Error
    ......... SSLCertVerificationError
    ......... ClipboardEmpty
    ......... MessageDefect
    ............ NoBoundaryInMultipartDefect
    ............ StartBoundaryNotFoundDefect
    ............ CloseBoundaryNotFoundDefect
    ............ FirstHeaderLineIsContinuationDefect
    ............ MisplacedEnvelopeHeaderDefect
    ............ MissingHeaderBodySeparatorDefect
    ............ MultipartInvariantViolationDefect
    ............ InvalidMultipartContentTransferEncodingDefect
    ............ UndecodableBytesDefect
    ............ InvalidBase64PaddingDefect
    ............ InvalidBase64CharactersDefect
    ............ InvalidBase64LengthDefect
    ............ HeaderDefect
    ............... InvalidHeaderDefect
    ............... HeaderMissingRequiredValue
    ............... NonPrintableDefect
    ............... ObsoleteHeaderDefect
    ............... NonASCIILocalPartDefect
    ......... IllegalMonthError
    ......... IllegalWeekdayError
    ......... MacroToEdit
    ...... AssertionError
    ...... ArithmeticError
    ......... FloatingPointError
    ......... OverflowError
    ......... ZeroDivisionError
    ............ DivisionByZero
    ............ DivisionUndefined
    ......... DecimalException
    ............ Clamped
    ............ Rounded
    ............... Underflow
    ............... Overflow
    ............ Inexact
    ............... Underflow
    ............... Overflow
    ............ Subnormal
    ............... Underflow
    ............ DivisionByZero
    ............ FloatOperation
    ............ InvalidOperation
    ............... ConversionSyntax
    ............... DivisionImpossible
    ............... DivisionUndefined
    ............... InvalidContext
    ...... SystemError
    ......... CodecRegistryError
    ...... ReferenceError
    ...... MemoryError
    ...... BufferError
    ...... Warning
    ......... UserWarning
    ............ GetPassWarning
    ............ FormatterWarning
    ......... DeprecationWarning
    ............ ProvisionalWarning
    ......... PendingDeprecationWarning
    ......... SyntaxWarning
    ......... RuntimeWarning
    ............ UnknownTimezoneWarning
    ......... FutureWarning
    ............ ProvisionalCompleterWarning
    ......... ImportWarning
    ......... UnicodeWarning
    ......... BytesWarning
    ......... ResourceWarning
    ......... DeprecatedTzFormatWarning
    ...... Error
    ...... _OptionError
    ...... _Error
    ...... error
    ...... Verbose
    ...... SubprocessError
    ......... CalledProcessError
    ......... TimeoutExpired
    ...... TokenError
    ...... StopTokenizing
    ...... Error
    ...... error
    ...... LZMAError
    ...... RegistryError
    ...... EndOfBlock
    ...... error
    ...... TraitError
    ...... ArgumentError
    ...... ArgumentTypeError
    ...... ConfigError
    ......... ConfigLoaderError
    ............ ArgumentError
    ......... ConfigFileNotFound
    ...... ConfigurableError
    ......... MultipleInstanceError
    ...... ApplicationError
    ...... ErrorDuringImport
    ...... BdbQuit
    ...... OptionError
    ...... Restart
    ...... ExceptionPexpect
    ......... EOF
    ......... TIMEOUT
    ...... error
    ...... PtyProcessError
    ...... FindCmdError
    ...... HomeDirError
    ...... ProfileDirError
    ...... IPythonCoreError
    ......... TryNext
    ......... UsageError
    ......... StdinNotImplementedError
    ...... InputRejected
    ...... GetoptError
    ...... Incomplete
    ...... ErrorToken
    ...... Error
    ......... CancelledError
    ......... TimeoutError
    ......... InvalidStateError
    ...... _GiveupOnSendfile
    ...... QueueEmpty
    ...... QueueFull
    ...... LimitOverrunError
    ...... _Stop
    ...... PickleError
    ......... PicklingError
    ......... UnpicklingError
    ...... PrefilterError
    ...... AliasError
    ......... InvalidAliasError
    ...... Error
    ......... InterfaceError
    ......... DatabaseError
    ............ InternalError
    ............ OperationalError
    ............ ProgrammingError
    ............ IntegrityError
    ............ DataError
    ............ NotSupportedError
    ...... Warning
    ...... SpaceInInput
    ...... TaskLocalNotSetError
    ...... InvalidStateError
    ...... Return
    ...... Empty
    ...... Full
    ...... NoRunningApplicationError
    ...... ValidationError
    ...... EditReadOnlyBuffer
    ...... _Retry
    ...... DOMException
    ......... IndexSizeErr
    ......... DomstringSizeErr
    ......... HierarchyRequestErr
    ......... WrongDocumentErr
    ......... InvalidCharacterErr
    ......... NoDataAllowedErr
    ......... NoModificationAllowedErr
    ......... NotFoundErr
    ......... NotSupportedErr
    ......... InuseAttributeErr
    ......... InvalidStateErr
    ......... SyntaxErr
    ......... InvalidModificationErr
    ......... NamespaceErr
    ......... InvalidAccessErr
    ......... ValidationErr
    ...... InvalidLayoutError
    ...... HeightIsUnknownError
    ...... ParserSyntaxError
    ...... InternalParseError
    ...... _PositionUpdatingFinished
    ...... UncaughtAttributeError
    ...... SimpleGetItemNotFound
    ...... ParamIssue
    ...... OnErrorLeaf
    ...... _JediError
    ......... InternalError
    ......... WrongVersion
    ...... InvalidPythonEnvironment
    ...... MessageError
    ......... MessageParseError
    ............ HeaderParseError
    ............ BoundaryError
    ......... MultipartConversionError
    ......... CharsetError
    ...... Error
    ...... HTTPException
    ......... NotConnected
    ......... InvalidURL
    ......... UnknownProtocol
    ......... UnknownTransferEncoding
    ......... UnimplementedFileMode
    ......... IncompleteRead
    ......... ImproperConnectionState
    ............ CannotSendRequest
    ............ CannotSendHeader
    ............ ResponseNotReady
    ......... BadStatusLine
    ............ RemoteDisconnected
    ......... LineTooLong
    ...... InteractivelyDefined
    ...... KillEmbedded
    ...... ArgumentError
    ...... ZMQBaseError
    ......... ZMQError
    ............ ContextTerminated
    ............ Again
    ............ InterruptedSystemCall
    ......... ZMQBindError
    ......... NotDone
    ...... NoIPAddresses
    ...... InvalidPortNumber
    ...... DuplicateKernelError
    ...... TimeoutError
    ...... error
    ...... ReturnValueIgnoredError
    ...... KeyReuseError
    ...... UnknownKeyError
    ...... LeakedCallbackError
    ...... BadYieldError
    ...... ReturnValueIgnoredError
    ...... Return
    ...... QueueEmpty
    ...... QueueFull
    ...... HostNotFound
    ... GeneratorExit
    ... SystemExit
    ... KeyboardInterrupt

