
Chapter 14: Introspection
=============================
_____________________________
Introspection or reflection is the ability of software to identify and report their own internal structures, such as types, variable scope, methods and attributes.

Native interpreter functions for introspection:
<table>
    <tr>
        <th>Function</th>
        <th>Returns</th>
    </tr>
    <tr>
        <td><code>type(object)</code></td>
        <td>The typo (class) of the object</td>
    </tr>
    <tr>
        <td><code>id(object)</code></td>
        <td>object identifier</td>
    </tr>
    <tr>
        <td><code>locals()</code></td>
        <td>local variables dictionary</td>
    </tr>
    <tr>
        <td><code>globals()</code></td>
        <td>global variables dictionary</td>
    </tr>
    <tr>
        <td><code>vars(object)</code></td>
        <td>object symbols dictionary</td>
    </tr>
    <tr>
        <td><code>len(object)</code></td>
        <td>size of an object</td>
    </tr>
    <tr>
        <td><code>dir(object)</code></td>
        <td>A list of object structures</td>
    </tr>
    <tr>
        <td><code>help(object)</code></td>
        <td>Object doc strings</td>
    </tr>
    <tr>
        <td><code>repr(object)</code></td>
        <td>Object representation</td>
    </tr>
    <tr>
        <td><code>isinstance(object, class)</code></td>
        <td>True if object is derived from class</td>
    </tr>
    <tr>
        <td><code>issubclass(subclass, class)</code></td>
        <td>True if object inherits the class</td>
    </tr>
</table>

The object identifier is a unique number that is used by the interpreter for identifying the objects internally.

    Example:


```python
# Getting some information
# about global objects in the program

from types import ModuleType

def info(n_obj):

    # Create a referênce to the object
    obj = globals()[n_obj]

    # Show object information 
    print ('Name of object:', n_obj)
    print ('Identifier:', id(obj))
    print ('Typo:', type(obj))
    print ('Representation:', repr(obj))

    # If it is a module
    if isinstance(obj, ModuleType):
        print( 'itens:')
        for item in dir(obj):
            print (item)
    print

# Showing information
for n_obj in dir()[:10]: # The slice [:10] is used just to limit objects
    info(n_obj)
```

    Name of object: In
    Identifier: 2514099592200
    Typo: <class 'list'>
    Representation: ['', "# Getting some information\n# about global objects in the program\n\nfrom types import ModuleType\n\ndef info(n_obj):\n\n    # Create a referênce to the object\n    obj = globals()[n_obj]\n\n    # Show object information \n    print 'Name of object:', n_obj\n    print 'Identifier:', id(obj)\n    print 'Typo:', type(obj)\n    print 'Representation:', repr(obj)\n\n    # If it is a module\n    if isinstance(obj, ModuleType):\n        print 'itens:'\n        for item in dir(obj):\n            print item\n    print\n\n# Showing information\nfor n_obj in dir()[:10]: # The slice [:10] is used just to limit objects\n    info(n_obj)", "# Getting some information\n# about global objects in the program\n\nfrom types import ModuleType\n\ndef info(n_obj):\n\n    # Create a referênce to the object\n    obj = globals()[n_obj]\n\n    # Show object information \n    print ('Name of object:', n_obj)\n    print ('Identifier:', id(obj))\n    print ('Typo:', type(obj))\n    print ('Representation:', repr(obj))\n\n    # If it is a module\n    if isinstance(obj, ModuleType):\n        print( 'itens:')\n        for item in dir(obj):\n            print (item)\n    print\n\n# Showing information\nfor n_obj in dir()[:10]: # The slice [:10] is used just to limit objects\n    info(n_obj)"]
    Name of object: ModuleType
    Identifier: 1983417472
    Typo: <class 'type'>
    Representation: <class 'module'>
    Name of object: Out
    Identifier: 2514099592776
    Typo: <class 'dict'>
    Representation: {}
    Name of object: _
    Identifier: 2514065726128
    Typo: <class 'str'>
    Representation: ''
    Name of object: __
    Identifier: 2514065726128
    Typo: <class 'str'>
    Representation: ''
    Name of object: ___
    Identifier: 2514065726128
    Typo: <class 'str'>
    Representation: ''
    Name of object: __builtin__
    Identifier: 2514065765864
    Typo: <class 'module'>
    Representation: <module 'builtins' (built-in)>
    itens:
    ArithmeticError
    AssertionError
    AttributeError
    BaseException
    BlockingIOError
    BrokenPipeError
    BufferError
    BytesWarning
    ChildProcessError
    ConnectionAbortedError
    ConnectionError
    ConnectionRefusedError
    ConnectionResetError
    DeprecationWarning
    EOFError
    Ellipsis
    EnvironmentError
    Exception
    False
    FileExistsError
    FileNotFoundError
    FloatingPointError
    FutureWarning
    GeneratorExit
    IOError
    ImportError
    ImportWarning
    IndentationError
    IndexError
    InterruptedError
    IsADirectoryError
    KeyError
    KeyboardInterrupt
    LookupError
    MemoryError
    NameError
    None
    NotADirectoryError
    NotImplemented
    NotImplementedError
    OSError
    OverflowError
    PendingDeprecationWarning
    PermissionError
    ProcessLookupError
    RecursionError
    ReferenceError
    ResourceWarning
    RuntimeError
    RuntimeWarning
    StopAsyncIteration
    StopIteration
    SyntaxError
    SyntaxWarning
    SystemError
    SystemExit
    TabError
    TimeoutError
    True
    TypeError
    UnboundLocalError
    UnicodeDecodeError
    UnicodeEncodeError
    UnicodeError
    UnicodeTranslateError
    UnicodeWarning
    UserWarning
    ValueError
    Warning
    WindowsError
    ZeroDivisionError
    __IPYTHON__
    __IPYTHON__active
    __build_class__
    __debug__
    __doc__
    __import__
    __loader__
    __name__
    __package__
    __spec__
    abs
    all
    any
    ascii
    bin
    bool
    bytearray
    bytes
    callable
    chr
    classmethod
    compile
    complex
    copyright
    credits
    delattr
    dict
    dir
    divmod
    dreload
    enumerate
    eval
    exec
    filter
    float
    format
    frozenset
    get_ipython
    getattr
    globals
    hasattr
    hash
    help
    hex
    id
    input
    int
    isinstance
    issubclass
    iter
    len
    license
    list
    locals
    map
    max
    memoryview
    min
    next
    object
    oct
    open
    ord
    pow
    print
    property
    range
    repr
    reversed
    round
    set
    setattr
    slice
    sorted
    staticmethod
    str
    sum
    super
    tuple
    type
    vars
    zip
    Name of object: __builtins__
    Identifier: 2514065765864
    Typo: <class 'module'>
    Representation: <module 'builtins' (built-in)>
    itens:
    ArithmeticError
    AssertionError
    AttributeError
    BaseException
    BlockingIOError
    BrokenPipeError
    BufferError
    BytesWarning
    ChildProcessError
    ConnectionAbortedError
    ConnectionError
    ConnectionRefusedError
    ConnectionResetError
    DeprecationWarning
    EOFError
    Ellipsis
    EnvironmentError
    Exception
    False
    FileExistsError
    FileNotFoundError
    FloatingPointError
    FutureWarning
    GeneratorExit
    IOError
    ImportError
    ImportWarning
    IndentationError
    IndexError
    InterruptedError
    IsADirectoryError
    KeyError
    KeyboardInterrupt
    LookupError
    MemoryError
    NameError
    None
    NotADirectoryError
    NotImplemented
    NotImplementedError
    OSError
    OverflowError
    PendingDeprecationWarning
    PermissionError
    ProcessLookupError
    RecursionError
    ReferenceError
    ResourceWarning
    RuntimeError
    RuntimeWarning
    StopAsyncIteration
    StopIteration
    SyntaxError
    SyntaxWarning
    SystemError
    SystemExit
    TabError
    TimeoutError
    True
    TypeError
    UnboundLocalError
    UnicodeDecodeError
    UnicodeEncodeError
    UnicodeError
    UnicodeTranslateError
    UnicodeWarning
    UserWarning
    ValueError
    Warning
    WindowsError
    ZeroDivisionError
    __IPYTHON__
    __IPYTHON__active
    __build_class__
    __debug__
    __doc__
    __import__
    __loader__
    __name__
    __package__
    __spec__
    abs
    all
    any
    ascii
    bin
    bool
    bytearray
    bytes
    callable
    chr
    classmethod
    compile
    complex
    copyright
    credits
    delattr
    dict
    dir
    divmod
    dreload
    enumerate
    eval
    exec
    filter
    float
    format
    frozenset
    get_ipython
    getattr
    globals
    hasattr
    hash
    help
    hex
    id
    input
    int
    isinstance
    issubclass
    iter
    len
    license
    list
    locals
    map
    max
    memoryview
    min
    next
    object
    oct
    open
    ord
    pow
    print
    property
    range
    repr
    reversed
    round
    set
    setattr
    slice
    sorted
    staticmethod
    str
    sum
    super
    tuple
    type
    vars
    zip
    Name of object: __doc__
    Identifier: 2514084256504
    Typo: <class 'str'>
    Representation: 'Automatically created module for IPython interactive environment'
    Name of object: __loader__
    Identifier: 1983419424
    Typo: <class 'NoneType'>
    Representation: None
    

Python also has a module called *types*, which has the definitions of the basic types of the interpreter.

Example:


```python
import types

s = ''
if isinstance(s, types.StringType):
    print 's is a string.'
```

    s is a string.
    

Through introspection, it is possible to determine the fields of a database table, for example.

Inspect
-------
The module *inspect* provides a set of high-level functions that allow for introspection to investigate types, collection items, classes, functions, source code and the runtime stack of the interpreter.

Example:


```python
import os.path
# inspect: "friendly" introspection module
import inspect

print 'Object:', inspect.getmodule(os.path)

print 'Class?', inspect.isclass(str)

# Lists all functions that exist in "os.path"

print 'Member:',

for name, struct in inspect.getmembers(os.path):

    if inspect.isfunction(struct):
        print name, 
```

    Object: <module 'posixpath' from '/home/csig/env/teste/lib/python2.7/posixpath.pyc'>
    Class? True
    Member: _joinrealpath abspath basename commonprefix dirname exists expanduser expandvars getatime getctime getmtime getsize isabs isdir isfile islink ismount join lexists normcase normpath realpath relpath samefile sameopenfile samestat split splitdrive splitext walk
    

The functions that work with the stack of the interpreter should be used with caution because it is possible to create cyclic references (a variable that points to the stack item that has the variable itself). The existence of references to stack items slows the destruction of the items by the garbage collector of the interpreter.


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
     table {
        width: 100%;
        margin: 0 !important;
        }  
     table th, table td {
        text-align: center !important;
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


