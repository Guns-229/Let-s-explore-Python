
# `_`, `__` and `__attr__` in Python

Certain classes of identifiers (besides keywords) have special meanings. These classes are identified by the patterns of leading and trailing underscore characters:

`_*`
Not imported by "from module import *". The special identifier "`_`" is used in the interactive interpreter to store the result of the last evaluation; it is stored in the `__builtin__` module. When not in interactive mode, "`_`" has no special meaning and is not defined. See section 6.12, ``The import statement.''
Note: The name "_" is often used in conjunction with internationalization; refer to the documentation for the gettext module for more information on this convention.

`__*__`
System-defined names. These names are defined by the interpreter and its implementation (including the standard library); applications should not expect to define additional names using this convention. The set of names of this class defined by Python may be extended in future versions. See section 3.4, ``Special method names.''

`__*`
Class-private names. Names in this category, when used within the context of a class definition, are re-written to use a mangled form to help avoid name clashes between **private** attributes of **base** and **derived** classes.
