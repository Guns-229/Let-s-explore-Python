
Chapter 8: Modules
=============================
_____________________________
For Python, modules are source files that can be imported into a program. They can contain any Python structure and **run when <span class="note" title="If it is necessary to run the module again during the execution of the application, it will have to be loaded again with the reload () function.">imported</span>**. They are compiled when first imported and stored in a file (with the extension ".pyc" or ".pyo"), have their own *namespaces*  and support *Doc Strings*. They are singleton objects (only one instance is loaded into memory, which is available globally for the program).

![Modules](files/bpyfd_diags6.png)

The modules are located by the interpreter through the list of folders `PYTHONPATH` (sys.path), which usually includes the current directory first.

The modules are loaded with the `import` statement. Thus, when using a module structure, it is necessary to identify the module. This is called absolute import.


```python
import os
print(type(os.name))
```

    <class 'str'>
    

You can also import modules with relative form:


```python
from os import name
print (type(name))
```

    <class 'str'>
    

> **NOTE**: To avoid problems such as variable obfuscation, the absolute import is considered a better programming practice than the relative import.

Example of module:


```python
# File calc.py

# Function defined in module
def average(list): return float(sum(list)) / len(list)
```

Example of module usage:


```python
# Imports calc module
import calc

l = [23, 54, 31, 77, 12, 34]

# Calls the function defined in calc
print (calc.average(l))
```

    38.5
    

The main module of a program has the variable `__name__` equals to `__main__`, thus it is possible to test if the main module:


```python
if __name__ == "__main__":
    # Code here will only be run 
    # if it is the main module
    # and not when it is imported by another program
    pass
```

That way it is easy to turn a program into a module.

Another module example:


```python
"""
modutils => utility routines for modules
"""

import os.path
import sys
import glob

def find(txt):
    """find modules with name containing the parameter."""

    resp = []

    for path in sys.path:
        mods = glob.glob('%s/*.py' % path)

        for mod in mods:
            if txt in os.path.basename(mod):
                resp.append(mod)

    return resp
```

Example module use:


```python
from os.path import getsize, getmtime
from time import localtime, asctime

import modutils

mods = modutils.find('os')
print("Valid attributes of module: ", dir(modutils))
for mod in mods:
    tm = asctime(localtime(getmtime(mod)))
    kb = getsize(mod) / 1024
    print ('{0}: ({1} kbytes, {2})'.format(mod, kb, tm))
```

    Valid attributes of module:  ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'find', 'glob', 'os', 'sys']
    /home/mayank/apps/python/lib/python3.5/os.py: (36.103515625 kbytes, Fri Oct 21 10:14:28 2016)
    /home/mayank/apps/python/lib/python3.5/posixpath.py: (14.5322265625 kbytes, Fri Oct 21 10:14:28 2016)
    /home/mayank/apps/python/lib/python3.5/_osx_support.py: (18.66015625 kbytes, Fri Oct 21 10:14:27 2016)
    /home/mayank/apps/python/lib/python3.5/site-packages/test_pycosat.py: (8.650390625 kbytes, Wed Dec  4 11:22:39 2013)
    /home/mayank/apps/python/lib/python3.5/site-packages/ecos.py: (2.3349609375 kbytes, Thu Sep 10 21:02:58 2015)
    

> _TIP_: Splitting programs into modules makes it easy to reuse and locate faults in the code.
