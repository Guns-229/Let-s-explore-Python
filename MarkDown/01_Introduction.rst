
Chapter 1 - Introduction to Python
==================================

--------------

`Python <http://www.python.org>`__ is a very **High Level,
object-oriented, dynamic1, strong typing2, interpreted** &
**interactive** programming language.

    1. Dynamic Programming language: It at runtime executes many common
       programming tasks which static programming languages perform
       during compilation such as

    -  Computation of code at runtime and late binding
    -  alteration of Objects at runtime
    -  Assembling of code at runtime based on the class of instances

    2. Strongly Typed: Typing errors are prevented at runtime using the
       implicit type conversion, also it don't have static type
       checking, i.e. compiler don't check or enforce type constraint
       rules. The term **duck typing** is now used to describe the
       dynamic typing paradigm. Duck typing is an application of the
       duck test in type safety. It requires that type checking be done
       at runtime only, and is implemented by use of dynamic typing or
       by reflection.

It is also an open source language (with license compatible with the
*General Public License (GPL)*, but less restrictive, allowing Python to
be even incorporated into proprietary products). Its specification is
maintained by the `Python Software
Foundation <http://www.python.org/psf/>`__ (PSF).

Key Features
------------

-  It uses an elegant syntax, making the code easier to read
-  Easy-to-use language that makes it simple to get code working. This
   makes it ideal for prototype development and other ad-hoc programming
   tasks, without compromising maintainability
-  Default installation contains large standard library which supports
   most of the common programming tasks, such as connecting to web
   servers, searching text with regular expressions, reading and
   modifying files etc
-  Python's interactive mode, makes it easy to validate snippets of
   code.
-  Bundled development environment called IDLE.
-  Is easily extended by adding new modules implemented in a compiled
   language such as C or C++.
-  Can also be embedded into an application to provide a programmable
   interface.
-  Runs anywhere, including Mac OS X, Windows, Linux, and Unix.
-  Is free software in two senses. It doesn't cost anything to download
   or use Python, or to include it in your application. It can be freely
   modified and re-distributed, because while the language is
   copyrighted it's available under an open source license.

Some programming-language features of Python are:
-------------------------------------------------

-  Many basic data types:
-  numbers (floating point, complex, and unlimited-length long integers)
-  strings (both ASCII and Unicode)
-  Collections (lists, dictionaries)
-  Python supports object-oriented programming with classes and multiple
   inheritance.
-  Code can be grouped into modules and packages.
-  The language supports raising and catching exceptions, resulting in
   cleaner error handling.
-  Data types are strongly and dynamically typed. Mixing incompatible
   types (e.g. attempting to add a string and a number) causes an
   exception to be raised, so errors are caught sooner.
-  Python contains advanced programming features such as generators and
   list comprehensions.
-  Python's automatic memory management frees you from having to
   manually allocate and free memory in your code.

It is possible to integrate Python with other languages such as C and
Fortran. In general terms, it has many similarities with other dynamic
languages such as Perl and Ruby.

History
-------

The language was created in 1990 by **Guido van Rossum**, at National
Research Institute for Mathematics and Computer Science in the
Netherlands (CWI) and had originally focused on users as physicists and
engineers. Python was designed from another existing language at the
time, called ABC. |Guido van Rossum|

.. |Guido van Rossum| image:: file://D:/code/LetsExplorePython/MarkDown/GuidoVanRossum.png

Versions
--------

The official implementation of Python is maintained by the PSF and
written in C, and therefore is also known as CPython. The latest stable
version is available for download at:

http://www.python.org/download/

For Windows platforms, simply run the installer. For other platforms,
such as Linux, Python is usually already part of the system, but in some
cases it may be necessary to compile and install the interpreter from
the source files.

There are also implementations of Python for. NET (IronPython), JVM
(Jython) and Python (PyPy).

## Running programs
-------------------

Example of Python program:

.. code:: python

    # the character "#" indicate that rest of the line is a comment 
    # and will be ignored by the interpreter
    
    # A list of musical instruments
    instruments = ['Drums', 'Flute', 'Harmonium', "Guitar"]
    
    # for each instrument in the list of instruments
    for instrument in instruments:
        print (instrument)


.. parsed-literal::

    Drums
    Flute
    Harmonium
    Guitar
    

In above example, ``instruments`` is a list containing the items
"Drums", "Flute", "Harmonium" and "Guitar" and as the ``for`` loop is
executed ``instrument`` corresponds to, an item from items on the list,
one at a time.

Executing the code
~~~~~~~~~~~~~~~~~~

The source files are usually identified by the extension ".py" and can
be run directly by the interpreter:

.. code:: sh

    python apl.py

Thus ``apl.py`` will run. On Windows, the file extensions ".py", ".
pyw", ". pyc" and ". pyo" are associated with Python automatically
during installation, so just click a the file to run it. The ". pyw"
files run with an alternate version of the interpreter that does not
open the console window.

Dynamic Typing
--------------

Python uses dynamic typing, which means that the type of a variable is
inferred by the interpreter at runtime (this is known as *Duck Typing*).
By the time a variable is created by attribution the interpreter defines
the type of a variable, along with the operations that can be applied.

Typing of Python is strong, ie, the interpreter checks whether the
transactions are valid and does automatic coercions between incompatible
types. In Python, coercions are performed automatically only between
types that are clearly related, as integer and long integer. To perform
the operation between non-compatible types, you must explicitly convert
the type of the variable or variables before the operation.

Compilation and interpretation
------------------------------

The source code is translated by Python to bytecode, which is a binary
format with instructions for the interpreter. The bytecode is cross
platform and can be distributed and run without the original source.

By default, the parser compiles the code and stores the bytecode on
disk, so the next time you run it, there is no need to recompile the
program, reducing the load time of execution. If the source files are
changed, the interpreter will be responsible for regenerating the
bytecode automatically, even using the *interactive shell*. When a
program or a module is invoked, the interpreter performs the analysis of
the code, converts to symbols, compiles (if there is no updated bytecode
on disk) and runs it in the Python virtual machine.

The bytecode is stored in files with the extension ". pyc" (normal
bytecode) or ". pyo" (optimized bytecode). The bytecode can also be
packaged along with an executable interpreter, to facilitate the
distribution of the application, eliminating the need to install Python
on each computer.

Interactive Mode
----------------

The Python interpreter can be used interactively, where lines of code
are typed into a *prompt* (command line) *shell* similar to the
operating system.

``python``

It is ready to receive commands after the appearance of the signal
``>>>`` on the screen:

``Python 2.6.4 (r264:75706, Nov  3 2009, 13:20:47)``\ 
``[GCC 4.4.1] on linux2``\ 
``Type "help", "copyright", "credits" or "license" for more information.``\ 
``>>>``

On Windows, the interactive mode is also available via the icon "Python
(command line)".

The interactive mode is a distinguishing feature of the language, as it
is possible to test and modify code snippets before inclusion in
programs, to extract and convert data or even analyze the state of the
objects in memory, among other possibilities.

Besides the traditional interactive mode of Python, there are other
programs that act as alternatives to more sophisticated interfaces (such
as PyCrust): [PyCrust] (files/pycrust.png)

Common IDE & Tools
------------------

There are many development tools for Python, such as IDEs, editors and
shells (that take advantage of the interactive capabilities of Python).

*Integrated Development Environments* (IDEs) are software packages that
integrate various development tools in an environment consistent with
the goal of increasing developer productivity. Generally, IDEs include
such features as syntax highlighting (colorized source code according to
the syntax of the language), source browsers, integrated shell and *code
completion* (the editor presents possible ways to complete the text it
can identify while typing). Among Python IDEs, there are most popular
ones:

-  `PyScripter <http://code.google.com/p/pyscripter/>`__
-  `Atom <https://atom.io>`__
-  `SPE <http://pythonide.blogspot.com/>`__ (Stani's Python Editor)
-  `Eric <http://eric-ide.python-projects.org/>`__
-  `PyDev <http://pydev.org/>`__ (plug-in for Eclipse IDE)
-  `vim <http://vim.org>`__
-  `Sublime Text <http://www.sublimetext.com/>`__

 [PyScripter] (files/pyscripter.png)

Entire list
~~~~~~~~~~~

(from
https://wiki.python.org/moin/IntegratedDevelopmentEnvironments?action=show&redirect=IDE)

+-------+-------+-------+-------+
| **Nam | **Pla | **Upd | **Not |
| e**   | tform | ated* | es**  |
|       | **    | *     |       |
+=======+=======+=======+=======+
| Thonn | Windo | 2016  | For   |
| y     | ws,   |       | teach |
|       | Linux |       | ing/l |
|       | ,     |       | earni |
|       | Mac   |       | ng    |
|       | OS X, |       | progr |
|       | more  |       | ammin |
|       |       |       | g.    |
|       |       |       | Focus |
|       |       |       | ed    |
|       |       |       | on    |
|       |       |       | progr |
|       |       |       | am    |
|       |       |       | runti |
|       |       |       | me    |
|       |       |       | visua |
|       |       |       | lizat |
|       |       |       | ion.  |
|       |       |       | Provi |
|       |       |       | des   |
|       |       |       | stepp |
|       |       |       | ing   |
|       |       |       | both  |
|       |       |       | in    |
|       |       |       | state |
|       |       |       | ments |
|       |       |       | and   |
|       |       |       | expre |
|       |       |       | ssion |
|       |       |       | s,    |
|       |       |       | no-ha |
|       |       |       | ssle  |
|       |       |       | varia |
|       |       |       | bles  |
|       |       |       | view, |
|       |       |       | separ |
|       |       |       | ate   |
|       |       |       | mode  |
|       |       |       | for   |
|       |       |       | expla |
|       |       |       | ining |
|       |       |       | refer |
|       |       |       | ences |
|       |       |       | etc.  |
+-------+-------+-------+-------+
| Komod | Windo | 2012  | Multi |
| o     | ws/Li |       | -lang |
|       | nux/M |       | uage  |
|       | ac    |       | IDE   |
|       | OS X  |       | with  |
|       |       |       | suppo |
|       |       |       | rt    |
|       |       |       | for   |
|       |       |       | Pytho |
|       |       |       | n     |
|       |       |       | 2.x   |
|       |       |       | and   |
|       |       |       | Pytho |
|       |       |       | n     |
|       |       |       | 3.    |
|       |       |       | Avail |
|       |       |       | able  |
|       |       |       | as    |
|       |       |       | Komod |
|       |       |       | o     |
|       |       |       | IDE   |
|       |       |       | (comm |
|       |       |       | ercia |
|       |       |       | l).   |
+-------+-------+-------+-------+
| LiCli | Linux | 2015  | Comme |
| pse   | /Mac  |       | rcial |
|       | OS    |       | Eclip |
|       | X/Win |       | se-ba |
|       | dows  |       | sed   |
|       |       |       | IDE   |
|       |       |       | which |
|       |       |       | provi |
|       |       |       | des   |
|       |       |       | a     |
|       |       |       | stand |
|       |       |       | alone |
|       |       |       | bundl |
|       |       |       | ing   |
|       |       |       | PyDev |
|       |       |       | ,     |
|       |       |       | Works |
|       |       |       | pace  |
|       |       |       | Mecha |
|       |       |       | nic,  |
|       |       |       | Eclip |
|       |       |       | se    |
|       |       |       | Color |
|       |       |       | Theme |
|       |       |       | ,     |
|       |       |       | Start |
|       |       |       | Explo |
|       |       |       | rer   |
|       |       |       | and   |
|       |       |       | AnyEd |
|       |       |       | it,   |
|       |       |       | along |
|       |       |       | with  |
|       |       |       | light |
|       |       |       | weigt |
|       |       |       | h     |
|       |       |       | suppo |
|       |       |       | rt    |
|       |       |       | for   |
|       |       |       | other |
|       |       |       | langu |
|       |       |       | ages, |
|       |       |       | and   |
|       |       |       | other |
|       |       |       | usabi |
|       |       |       | lity  |
|       |       |       | enhan |
|       |       |       | cemen |
|       |       |       | ts    |
|       |       |       | (such |
|       |       |       | as    |
|       |       |       | multi |
|       |       |       | -care |
|       |       |       | t-edi |
|       |       |       | tion) |
|       |       |       | .     |
+-------+-------+-------+-------+
| NetBe | Linux | 2009  | Pytho |
| ans   | ,     |       | n/Jyt |
|       | Mac,  |       | hon   |
|       | Solar |       | suppo |
|       | is,   |       | rt    |
|       | Windo |       | in    |
|       | ws    |       | NetBe |
|       |       |       | ans   |
|       |       |       | --    |
|       |       |       | Open  |
|       |       |       | sourc |
|       |       |       | e,    |
|       |       |       | allow |
|       |       |       | s     |
|       |       |       | Pytho |
|       |       |       | n     |
|       |       |       | and   |
|       |       |       | Jytho |
|       |       |       | n     |
|       |       |       | Editi |
|       |       |       | ng,   |
|       |       |       | code- |
|       |       |       | compl |
|       |       |       | etion |
|       |       |       | ,     |
|       |       |       | debug |
|       |       |       | ger,  |
|       |       |       | refac |
|       |       |       | torin |
|       |       |       | g,    |
|       |       |       | templ |
|       |       |       | ates, |
|       |       |       | synta |
|       |       |       | x     |
|       |       |       | analy |
|       |       |       | sis,  |
|       |       |       | etc.; |
|       |       |       | see   |
|       |       |       | also  |
|       |       |       | http: |
|       |       |       | //wik |
|       |       |       | i.net |
|       |       |       | beans |
|       |       |       | .org/ |
|       |       |       | Pytho |
|       |       |       | n.    |
|       |       |       | UPDAT |
|       |       |       | E:    |
|       |       |       | Netbe |
|       |       |       | ans   |
|       |       |       | 7.0   |
|       |       |       | relea |
|       |       |       | sed   |
|       |       |       | witho |
|       |       |       | ut    |
|       |       |       | Pytho |
|       |       |       | n     |
|       |       |       | suppo |
|       |       |       | rt.   |
|       |       |       | Check |
|       |       |       | http: |
|       |       |       | //wik |
|       |       |       | i.net |
|       |       |       | beans |
|       |       |       | .org/ |
|       |       |       | Pytho |
|       |       |       | n70Ro |
|       |       |       | admap |
|       |       |       | for   |
|       |       |       | upcom |
|       |       |       | ing   |
|       |       |       | Pytho |
|       |       |       | n     |
|       |       |       | suppo |
|       |       |       | rt.   |
+-------+-------+-------+-------+
| PyCha | Linux | 2014  | Free  |
| rm    | /Mac  |       | open- |
|       | OS    |       | sourc |
|       | X/Win |       | e     |
|       | dows  |       | IDE   |
|       |       |       | with  |
|       |       |       | a     |
|       |       |       | smart |
|       |       |       | Pytho |
|       |       |       | n     |
|       |       |       | edito |
|       |       |       | r     |
|       |       |       | provi |
|       |       |       | ding  |
|       |       |       | quick |
|       |       |       | code  |
|       |       |       | navig |
|       |       |       | ation |
|       |       |       | ,     |
|       |       |       | code  |
|       |       |       | compl |
|       |       |       | etion |
|       |       |       | ,     |
|       |       |       | refac |
|       |       |       | torin |
|       |       |       | g,    |
|       |       |       | unit  |
|       |       |       | testi |
|       |       |       | ng    |
|       |       |       | and   |
|       |       |       | debug |
|       |       |       | ger.  |
|       |       |       | Has a |
|       |       |       | comme |
|       |       |       | rcial |
|       |       |       | Profe |
|       |       |       | ssion |
|       |       |       | al    |
|       |       |       | editi |
|       |       |       | on    |
|       |       |       | that  |
|       |       |       | fully |
|       |       |       | suppo |
|       |       |       | rts   |
|       |       |       | Web   |
|       |       |       | devel |
|       |       |       | opmen |
|       |       |       | t     |
|       |       |       | with  |
|       |       |       | Djang |
|       |       |       | o,    |
|       |       |       | Flask |
|       |       |       | ,     |
|       |       |       | Mako  |
|       |       |       | and   |
|       |       |       | Web2P |
|       |       |       | y     |
|       |       |       | and   |
|       |       |       | allow |
|       |       |       | s     |
|       |       |       | to    |
|       |       |       | devel |
|       |       |       | op    |
|       |       |       | remot |
|       |       |       | ely.  |
|       |       |       | Free  |
|       |       |       | PyCha |
|       |       |       | rm    |
|       |       |       | profe |
|       |       |       | ssion |
|       |       |       | al    |
|       |       |       | licen |
|       |       |       | ses   |
|       |       |       | for   |
|       |       |       | open- |
|       |       |       | sourc |
|       |       |       | e     |
|       |       |       | proje |
|       |       |       | cts.  |
+-------+-------+-------+-------+
| Pytho | Linux | 2016  | Free  |
| n     | /Mac  |       | open- |
| for   | OS    |       | sourc |
| VS    | X/Win |       | e     |
| Code  | dows  |       | exten |
|       |       |       | sion  |
|       |       |       | for   |
|       |       |       | Visua |
|       |       |       | l     |
|       |       |       | Studi |
|       |       |       | o     |
|       |       |       | Code. |
|       |       |       | Suppo |
|       |       |       | rts   |
|       |       |       | synta |
|       |       |       | x     |
|       |       |       | highl |
|       |       |       | ighti |
|       |       |       | ng,   |
|       |       |       | debug |
|       |       |       | ging, |
|       |       |       | code  |
|       |       |       | compl |
|       |       |       | etion |
|       |       |       | ,     |
|       |       |       | code  |
|       |       |       | navig |
|       |       |       | ation |
|       |       |       | ,     |
|       |       |       | refac |
|       |       |       | torin |
|       |       |       | g,    |
|       |       |       | with  |
|       |       |       | suppo |
|       |       |       | rt    |
|       |       |       | for   |
|       |       |       | Djang |
|       |       |       | o,    |
|       |       |       | multi |
|       |       |       | threa |
|       |       |       | ded,  |
|       |       |       | local |
|       |       |       | and   |
|       |       |       | remot |
|       |       |       | e     |
|       |       |       | debug |
|       |       |       | ging. |
+-------+-------+-------+-------+
| KDeve | Linux | 2014  | Free  |
| lop   | /Mac  |       | open- |
|       | OS    |       | sourc |
|       | X/(Wi |       | e     |
|       | ndows |       | IDE   |
|       | )     |       | with  |
|       |       |       | a     |
|       |       |       | focus |
|       |       |       | on    |
|       |       |       | stati |
|       |       |       | c     |
|       |       |       | analy |
|       |       |       | sis-b |
|       |       |       | ased  |
|       |       |       | code  |
|       |       |       | compl |
|       |       |       | etion |
|       |       |       | ,     |
|       |       |       | navig |
|       |       |       | ation |
|       |       |       | and   |
|       |       |       | highl |
|       |       |       | ighti |
|       |       |       | ng.   |
|       |       |       | Also  |
|       |       |       | featu |
|       |       |       | res   |
|       |       |       | a VI  |
|       |       |       | emula |
|       |       |       | tion  |
|       |       |       | mode. |
+-------+-------+-------+-------+
| PyDev | Eclip | 2015  | Free, |
|       | se    |       | open- |
|       |       |       | sourc |
|       |       |       | e     |
|       |       |       | plugi |
|       |       |       | n     |
|       |       |       | for   |
|       |       |       | Eclip |
|       |       |       | se    |
|       |       |       | --    |
|       |       |       | Allow |
|       |       |       | s     |
|       |       |       | Pytho |
|       |       |       | n,    |
|       |       |       | Jytho |
|       |       |       | n,    |
|       |       |       | and   |
|       |       |       | IronP |
|       |       |       | ython |
|       |       |       | editi |
|       |       |       | ng,   |
|       |       |       | code- |
|       |       |       | compl |
|       |       |       | etion |
|       |       |       | ,     |
|       |       |       | debug |
|       |       |       | ger,  |
|       |       |       | refac |
|       |       |       | torin |
|       |       |       | g,    |
|       |       |       | quick |
|       |       |       | navig |
|       |       |       | ation |
|       |       |       | ,     |
|       |       |       | templ |
|       |       |       | ates, |
|       |       |       | code  |
|       |       |       | analy |
|       |       |       | sis,  |
|       |       |       | unitt |
|       |       |       | est   |
|       |       |       | integ |
|       |       |       | ratio |
|       |       |       | n,    |
|       |       |       | Djang |
|       |       |       | o     |
|       |       |       | integ |
|       |       |       | ratio |
|       |       |       | n,    |
|       |       |       | etc.  |
+-------+-------+-------+-------+
| Wing  | Windo | 2016  | Comme |
| IDE   | ws,   |       | rcial |
|       | Linux |       | Pytho |
|       | ,     |       | n     |
|       | Mac   |       | IDE   |
|       | OS X  |       | with  |
|       |       |       | advan |
|       |       |       | ced   |
|       |       |       | debug |
|       |       |       | ger,  |
|       |       |       | edito |
|       |       |       | r     |
|       |       |       | with  |
|       |       |       | vi,   |
|       |       |       | emacs |
|       |       |       | ,     |
|       |       |       | visua |
|       |       |       | l     |
|       |       |       | studi |
|       |       |       | o     |
|       |       |       | and   |
|       |       |       | other |
|       |       |       | key   |
|       |       |       | bindi |
|       |       |       | ngs,  |
|       |       |       | auto- |
|       |       |       | compl |
|       |       |       | etion |
|       |       |       | ,     |
|       |       |       | auto- |
|       |       |       | editi |
|       |       |       | ng,   |
|       |       |       | snipp |
|       |       |       | ets,  |
|       |       |       | goto- |
|       |       |       | defin |
|       |       |       | ition |
|       |       |       | ,     |
|       |       |       | find  |
|       |       |       | uses, |
|       |       |       | refac |
|       |       |       | torin |
|       |       |       | g,    |
|       |       |       | unit  |
|       |       |       | testi |
|       |       |       | ng,   |
|       |       |       | sourc |
|       |       |       | e     |
|       |       |       | brows |
|       |       |       | er,   |
|       |       |       | and   |
|       |       |       | much  |
|       |       |       | more. |
|       |       |       | There |
|       |       |       | are   |
|       |       |       | sever |
|       |       |       | al    |
|       |       |       | produ |
|       |       |       | ct    |
|       |       |       | level |
|       |       |       | s,    |
|       |       |       | inclu |
|       |       |       | ding  |
|       |       |       | free  |
|       |       |       | and   |
|       |       |       | paid  |
|       |       |       | versi |
|       |       |       | ons   |
|       |       |       | with  |
|       |       |       | a     |
|       |       |       | fully |
|       |       |       | funct |
|       |       |       | ional |
|       |       |       | trial |
|       |       |       | with  |
|       |       |       | up to |
|       |       |       | three |
|       |       |       | 10    |
|       |       |       | day   |
|       |       |       | trial |
|       |       |       | perio |
|       |       |       | ds.   |
|       |       |       | See   |
|       |       |       | produ |
|       |       |       | ct    |
|       |       |       | featu |
|       |       |       | res   |
|       |       |       | and   |
|       |       |       | prici |
|       |       |       | ng    |
|       |       |       | for   |
|       |       |       | detai |
|       |       |       | ls.   |
+-------+-------+-------+-------+
| PyScr | Windo | 2012  | MIT   |
| ipter | ws    |       | licen |
|       |       |       | sed   |
|       |       |       | IDE   |
|       |       |       | writt |
|       |       |       | en    |
|       |       |       | in    |
|       |       |       | Delph |
|       |       |       | i     |
|       |       |       | with  |
|       |       |       | debug |
|       |       |       | ger,  |
|       |       |       | integ |
|       |       |       | rated |
|       |       |       | unit  |
|       |       |       | testi |
|       |       |       | ng,   |
|       |       |       | sourc |
|       |       |       | e     |
|       |       |       | brows |
|       |       |       | er,   |
|       |       |       | code  |
|       |       |       | navig |
|       |       |       | ation |
|       |       |       | and   |
|       |       |       | synta |
|       |       |       | x     |
|       |       |       | color |
|       |       |       | ing/a |
|       |       |       | uto-c |
|       |       |       | omple |
|       |       |       | ting  |
|       |       |       | edito |
|       |       |       | r.    |
+-------+-------+-------+-------+
| Pyshi | Windo | 2010  | Comme |
| eld   | ws,   |       | rcial |
|       | Linux |       | IDE   |
|       |       |       | tool  |
|       |       |       | used  |
|       |       |       | to    |
|       |       |       | edit, |
|       |       |       | debug |
|       |       |       | Pytho |
|       |       |       | n     |
|       |       |       | scrip |
|       |       |       | t,    |
|       |       |       | publi |
|       |       |       | sh    |
|       |       |       | encry |
|       |       |       | pted  |
|       |       |       | scrip |
|       |       |       | ts,   |
|       |       |       | build |
|       |       |       | a     |
|       |       |       | stand |
|       |       |       | alone |
|       |       |       | execu |
|       |       |       | table |
|       |       |       | file, |
|       |       |       | manag |
|       |       |       | e     |
|       |       |       | more  |
|       |       |       | files |
|       |       |       | by    |
|       |       |       | proje |
|       |       |       | ct    |
|       |       |       | view, |
|       |       |       | and   |
|       |       |       | make  |
|       |       |       | insta |
|       |       |       | llati |
|       |       |       | on    |
|       |       |       | in    |
|       |       |       | vario |
|       |       |       | us    |
|       |       |       | forms |
|       |       |       | (.msi |
|       |       |       | ,     |
|       |       |       | .tar. |
|       |       |       | gz,   |
|       |       |       | .rpm, |
|       |       |       | .zip, |
|       |       |       | .tar. |
|       |       |       | bz2). |
|       |       |       | It    |
|       |       |       | inclu |
|       |       |       | des   |
|       |       |       | an    |
|       |       |       | edito |
|       |       |       | r     |
|       |       |       | simul |
|       |       |       | ating |
|       |       |       | Emacs |
|       |       |       | pytho |
|       |       |       | n-mod |
|       |       |       | e,    |
|       |       |       | a GUI |
|       |       |       | debug |
|       |       |       | ger   |
|       |       |       | simul |
|       |       |       | ating |
|       |       |       | GDB,  |
|       |       |       | a     |
|       |       |       | proje |
|       |       |       | ct    |
|       |       |       | view  |
|       |       |       | used  |
|       |       |       | to    |
|       |       |       | manag |
|       |       |       | e     |
|       |       |       | scrip |
|       |       |       | ts,   |
|       |       |       | modul |
|       |       |       | es,   |
|       |       |       | exten |
|       |       |       | sions |
|       |       |       | ,     |
|       |       |       | packa |
|       |       |       | ges,  |
|       |       |       | platf |
|       |       |       | orm   |
|       |       |       | speci |
|       |       |       | fic   |
|       |       |       | data  |
|       |       |       | files |
|       |       |       | ,     |
|       |       |       | and   |
|       |       |       | GUI   |
|       |       |       | inter |
|       |       |       | face  |
|       |       |       | to    |
|       |       |       | make  |
|       |       |       | insta |
|       |       |       | llati |
|       |       |       | on.   |
+-------+-------+-------+-------+
| Spyde | Windo | 2012  | Free  |
| r     | ws/Li |       | open- |
|       | nux/M |       | sourc |
|       | ac    |       | e     |
|       | OS X  |       | scien |
|       |       |       | tific |
|       |       |       | Pytho |
|       |       |       | n     |
|       |       |       | devel |
|       |       |       | opmen |
|       |       |       | t     |
|       |       |       | envir |
|       |       |       | onmen |
|       |       |       | t     |
|       |       |       | provi |
|       |       |       | ding  |
|       |       |       | MATLA |
|       |       |       | B-lik |
|       |       |       | e     |
|       |       |       | featu |
|       |       |       | res:  |
|       |       |       | conso |
|       |       |       | le    |
|       |       |       | with  |
|       |       |       | varia |
|       |       |       | ble   |
|       |       |       | brows |
|       |       |       | er,   |
|       |       |       | sys.p |
|       |       |       | ath   |
|       |       |       | brows |
|       |       |       | er,   |
|       |       |       | envir |
|       |       |       | onmen |
|       |       |       | t     |
|       |       |       | varia |
|       |       |       | bles  |
|       |       |       | brows |
|       |       |       | er,   |
|       |       |       | integ |
|       |       |       | rated |
|       |       |       | plott |
|       |       |       | ing   |
|       |       |       | featu |
|       |       |       | res,  |
|       |       |       | autoc |
|       |       |       | omple |
|       |       |       | tion  |
|       |       |       | and   |
|       |       |       | toolt |
|       |       |       | ips   |
|       |       |       | -     |
|       |       |       | edito |
|       |       |       | r     |
|       |       |       | with  |
|       |       |       | synta |
|       |       |       | x     |
|       |       |       | highl |
|       |       |       | ighti |
|       |       |       | ng,   |
|       |       |       | class |
|       |       |       | /func |
|       |       |       | tion  |
|       |       |       | brows |
|       |       |       | er,   |
|       |       |       | pyfla |
|       |       |       | kes/p |
|       |       |       | ylint |
|       |       |       | code  |
|       |       |       | analy |
|       |       |       | sis,  |
|       |       |       | inlin |
|       |       |       | e     |
|       |       |       | find/ |
|       |       |       | repla |
|       |       |       | ce    |
|       |       |       | and   |
|       |       |       | searc |
|       |       |       | h     |
|       |       |       | in    |
|       |       |       | files |
|       |       |       | featu |
|       |       |       | res,  |
|       |       |       | code  |
|       |       |       | compl |
|       |       |       | etion |
|       |       |       | and   |
|       |       |       | toolt |
|       |       |       | ips.  |
|       |       |       | 100%  |
|       |       |       | pure  |
|       |       |       | Pytho |
|       |       |       | n,    |
|       |       |       | part  |
|       |       |       | of    |
|       |       |       | Pytho |
|       |       |       | n(x,y |
|       |       |       | )     |
|       |       |       | distr |
|       |       |       | ibuti |
|       |       |       | on    |
|       |       |       | (Wind |
|       |       |       | ows/L |
|       |       |       | inux) |
|       |       |       | .     |
+-------+-------+-------+-------+
| IDLE  | Windo | 2009  | Multi |
|       | ws/Li |       | -wind |
|       | nux/M |       | ow    |
|       | ac    |       | color |
|       | OS    |       | ized  |
|       | X/All |       | sourc |
|       | Tk    |       | e     |
|       | Platf |       | brows |
|       | orms  |       | er,   |
|       |       |       | autoi |
|       |       |       | ndent |
|       |       |       | ,     |
|       |       |       | autoc |
|       |       |       | omple |
|       |       |       | tion, |
|       |       |       | tool  |
|       |       |       | tips, |
|       |       |       | code  |
|       |       |       | conte |
|       |       |       | xt    |
|       |       |       | panel |
|       |       |       | ,     |
|       |       |       | searc |
|       |       |       | h     |
|       |       |       | in    |
|       |       |       | files |
|       |       |       | ,     |
|       |       |       | class |
|       |       |       | and   |
|       |       |       | path  |
|       |       |       | brows |
|       |       |       | ers,  |
|       |       |       | debug |
|       |       |       | ger,  |
|       |       |       | execu |
|       |       |       | tes   |
|       |       |       | code  |
|       |       |       | in    |
|       |       |       | clean |
|       |       |       | separ |
|       |       |       | ate   |
|       |       |       | subpr |
|       |       |       | ocess |
|       |       |       | with  |
|       |       |       | one   |
|       |       |       | keyst |
|       |       |       | roke. |
|       |       |       | 100%  |
|       |       |       | pure  |
|       |       |       | Pytho |
|       |       |       | n,    |
|       |       |       | part  |
|       |       |       | of    |
|       |       |       | Pytho |
|       |       |       | n     |
|       |       |       | 2.x   |
|       |       |       | and   |
|       |       |       | 3.x   |
|       |       |       | distr |
|       |       |       | ibuti |
|       |       |       | ons.  |
+-------+-------+-------+-------+
| IdleX | Windo | 2012  | IdleX |
|       | ws/Li |       | is a  |
|       | nux/M |       | colle |
|       | ac    |       | ction |
|       | OS    |       | of    |
|       | X/All |       | over  |
|       | Tk    |       | twent |
|       | Platf |       | y     |
|       | orms  |       | exten |
|       |       |       | sions |
|       |       |       | and   |
|       |       |       | plugi |
|       |       |       | ns    |
|       |       |       | that  |
|       |       |       | provi |
|       |       |       | de    |
|       |       |       | addit |
|       |       |       | ional |
|       |       |       | funct |
|       |       |       | ional |
|       |       |       | ity   |
|       |       |       | to    |
|       |       |       | IDLE, |
|       |       |       | a     |
|       |       |       | Pytho |
|       |       |       | n     |
|       |       |       | IDE   |
|       |       |       | provi |
|       |       |       | ded   |
|       |       |       | in    |
|       |       |       | the   |
|       |       |       | stand |
|       |       |       | ard   |
|       |       |       | libra |
|       |       |       | ry.   |
|       |       |       | It    |
|       |       |       | trans |
|       |       |       | forms |
|       |       |       | IDLE  |
|       |       |       | into  |
|       |       |       | a     |
|       |       |       | more  |
|       |       |       | usefu |
|       |       |       | l     |
|       |       |       | tool  |
|       |       |       | for   |
|       |       |       | acade |
|       |       |       | mic   |
|       |       |       | resea |
|       |       |       | rch   |
|       |       |       | and   |
|       |       |       | devel |
|       |       |       | opmen |
|       |       |       | t     |
|       |       |       | as    |
|       |       |       | well  |
|       |       |       | as    |
|       |       |       | explo |
|       |       |       | rator |
|       |       |       | y     |
|       |       |       | progr |
|       |       |       | ammin |
|       |       |       | g.    |
+-------+-------+-------+-------+
| µ.dev | Windo | 2010  | An    |
|       | ws    |       | open- |
|       | (need |       | sourc |
|       | s     |       | e     |
|       | to be |       | IDE,  |
|       | compi |       | creat |
|       | led   |       | ed    |
|       | manua |       | using |
|       | lly   |       | Lazar |
|       | for   |       | us.   |
|       | other |       | It's  |
|       | platf |       | only  |
|       | orms) |       | for   |
|       |       |       | Pytho |
|       |       |       | n.    |
|       |       |       | inclu |
|       |       |       | de    |
|       |       |       | synta |
|       |       |       | x     |
|       |       |       | highl |
|       |       |       | ighti |
|       |       |       | ng,   |
|       |       |       | proje |
|       |       |       | ct    |
|       |       |       | manag |
|       |       |       | er,   |
|       |       |       | and   |
|       |       |       | uses  |
|       |       |       | pdb   |
|       |       |       | for   |
|       |       |       | debug |
|       |       |       | ging. |
+-------+-------+-------+-------+
| Pyzo  | Windo | 2016  | Open- |
| (form | ws/Li |       | sourc |
| erly  | nux/M |       | e     |
| IEP)  | ac    |       | Pytho |
|       | OS X  |       | n     |
|       |       |       | IDE   |
|       |       |       | focus |
|       |       |       | ed    |
|       |       |       | on    |
|       |       |       | inter |
|       |       |       | activ |
|       |       |       | ity   |
|       |       |       | and   |
|       |       |       | intro |
|       |       |       | spect |
|       |       |       | ion,  |
|       |       |       | which |
|       |       |       | makes |
|       |       |       | it    |
|       |       |       | very  |
|       |       |       | suita |
|       |       |       | ble   |
|       |       |       | for   |
|       |       |       | scien |
|       |       |       | tific |
|       |       |       | compu |
|       |       |       | ting. |
|       |       |       | Its   |
|       |       |       | pract |
|       |       |       | ical  |
|       |       |       | desig |
|       |       |       | n     |
|       |       |       | is    |
|       |       |       | aimed |
|       |       |       | at    |
|       |       |       | simpl |
|       |       |       | icity |
|       |       |       | and   |
|       |       |       | effic |
|       |       |       | iency |
|       |       |       | .     |
|       |       |       | Pyzo  |
|       |       |       | consi |
|       |       |       | sts   |
|       |       |       | of    |
|       |       |       | two   |
|       |       |       | main  |
|       |       |       | compo |
|       |       |       | nents |
|       |       |       | ,     |
|       |       |       | the   |
|       |       |       | edito |
|       |       |       | r     |
|       |       |       | and   |
|       |       |       | the   |
|       |       |       | shell |
|       |       |       | ,     |
|       |       |       | and   |
|       |       |       | uses  |
|       |       |       | a set |
|       |       |       | of    |
|       |       |       | plugg |
|       |       |       | able  |
|       |       |       | tools |
|       |       |       | to    |
|       |       |       | help  |
|       |       |       | the   |
|       |       |       | progr |
|       |       |       | ammer |
|       |       |       | in    |
|       |       |       | vario |
|       |       |       | us    |
|       |       |       | ways: |
|       |       |       | e.g.  |
|       |       |       | sourc |
|       |       |       | e     |
|       |       |       | struc |
|       |       |       | ture, |
|       |       |       | inter |
|       |       |       | activ |
|       |       |       | e     |
|       |       |       | help, |
|       |       |       | works |
|       |       |       | pace, |
|       |       |       | file  |
|       |       |       | brows |
|       |       |       | er    |
|       |       |       | (with |
|       |       |       | funct |
|       |       |       | ional |
|       |       |       | ity   |
|       |       |       | for   |
|       |       |       | searc |
|       |       |       | hing) |
|       |       |       | .     |
|       |       |       | Also  |
|       |       |       | inclu |
|       |       |       | des   |
|       |       |       | a     |
|       |       |       | post- |
|       |       |       | morte |
|       |       |       | m     |
|       |       |       | debug |
|       |       |       | ger.  |
+-------+-------+-------+-------+
| Pytho | Windo | 2011  | An    |
| nTool | ws/Li |       | inter |
| kit   | nux/M |       | activ |
| (PTK) | ac    |       | e     |
|       | OS X  |       | envir |
|       |       |       | onmen |
|       |       |       | t     |
|       |       |       | for   |
|       |       |       | pytho |
|       |       |       | n     |
|       |       |       | built |
|       |       |       | aroun |
|       |       |       | d     |
|       |       |       | a     |
|       |       |       | matla |
|       |       |       | b     |
|       |       |       | style |
|       |       |       | conso |
|       |       |       | le    |
|       |       |       | windo |
|       |       |       | w     |
|       |       |       | and   |
|       |       |       | edito |
|       |       |       | r.    |
|       |       |       | It    |
|       |       |       | was   |
|       |       |       | desig |
|       |       |       | ned   |
|       |       |       | to    |
|       |       |       | provi |
|       |       |       | de    |
|       |       |       | a     |
|       |       |       | pytho |
|       |       |       | n     |
|       |       |       | based |
|       |       |       | envir |
|       |       |       | onmen |
|       |       |       | t     |
|       |       |       | simil |
|       |       |       | iar   |
|       |       |       | to    |
|       |       |       | Matla |
|       |       |       | b     |
|       |       |       | for   |
|       |       |       | scien |
|       |       |       | tists |
|       |       |       | and   |
|       |       |       | engin |
|       |       |       | eers  |
|       |       |       | howev |
|       |       |       | er    |
|       |       |       | it    |
|       |       |       | can   |
|       |       |       | also  |
|       |       |       | be    |
|       |       |       | used  |
|       |       |       | as a  |
|       |       |       | gener |
|       |       |       | al    |
|       |       |       | purpo |
|       |       |       | se    |
|       |       |       | inter |
|       |       |       | activ |
|       |       |       | e     |
|       |       |       | pytho |
|       |       |       | n     |
|       |       |       | envir |
|       |       |       | onmen |
|       |       |       | t     |
|       |       |       | espec |
|       |       |       | ially |
|       |       |       | for   |
|       |       |       | inter |
|       |       |       | activ |
|       |       |       | e     |
|       |       |       | GUI   |
|       |       |       | progr |
|       |       |       | ammin |
|       |       |       | g.    |
|       |       |       | Featu |
|       |       |       | res   |
|       |       |       | inclu |
|       |       |       | de:   |
|       |       |       | Multi |
|       |       |       | ple   |
|       |       |       | indep |
|       |       |       | enden |
|       |       |       | t     |
|       |       |       | pytho |
|       |       |       | n     |
|       |       |       | inter |
|       |       |       | prete |
|       |       |       | rs.   |
|       |       |       | Inter |
|       |       |       | activ |
|       |       |       | ely   |
|       |       |       | progr |
|       |       |       | am    |
|       |       |       | with  |
|       |       |       | diffe |
|       |       |       | rent  |
|       |       |       | GUI   |
|       |       |       | toolk |
|       |       |       | its   |
|       |       |       | (wxPy |
|       |       |       | thon, |
|       |       |       | TkInt |
|       |       |       | er,   |
|       |       |       | pyGTK |
|       |       |       | ,     |
|       |       |       | pyQT4 |
|       |       |       | and   |
|       |       |       | PySid |
|       |       |       | e).   |
|       |       |       | Matla |
|       |       |       | b     |
|       |       |       | style |
|       |       |       | names |
|       |       |       | pace/ |
|       |       |       | works |
|       |       |       | pace  |
|       |       |       | brows |
|       |       |       | er.   |
|       |       |       | Objec |
|       |       |       | t     |
|       |       |       | auto- |
|       |       |       | compl |
|       |       |       | etion |
|       |       |       | s,    |
|       |       |       | callt |
|       |       |       | ips   |
|       |       |       | and   |
|       |       |       | multi |
|       |       |       | -line |
|       |       |       | comma |
|       |       |       | nd    |
|       |       |       | editi |
|       |       |       | ng    |
|       |       |       | in    |
|       |       |       | the   |
|       |       |       | conso |
|       |       |       | le.   |
|       |       |       | Objec |
|       |       |       | t     |
|       |       |       | inspe |
|       |       |       | ction |
|       |       |       | and   |
|       |       |       | pytho |
|       |       |       | n     |
|       |       |       | path  |
|       |       |       | manag |
|       |       |       | ement |
|       |       |       | .     |
|       |       |       | Simpl |
|       |       |       | e     |
|       |       |       | code  |
|       |       |       | edito |
|       |       |       | r     |
|       |       |       | and   |
|       |       |       | integ |
|       |       |       | rated |
|       |       |       | debug |
|       |       |       | ger.  |
+-------+-------+-------+-------+
| PyStu | Windo | 2012  | Open- |
| dio   | ws/Li |       | sourc |
|       | nux/M |       | e     |
|       | ac    |       | plugi |
|       | OS X  |       | n     |
|       |       |       | that  |
|       |       |       | adds  |
|       |       |       | synta |
|       |       |       | x     |
|       |       |       | check |
|       |       |       | ing,  |
|       |       |       | integ |
|       |       |       | rated |
|       |       |       | debug |
|       |       |       | ger   |
|       |       |       | and   |
|       |       |       | modul |
|       |       |       | e     |
|       |       |       | searc |
|       |       |       | h     |
|       |       |       | to    |
|       |       |       | Editr |
|       |       |       | a,    |
|       |       |       | a     |
|       |       |       | gener |
|       |       |       | al    |
|       |       |       | purpo |
|       |       |       | se    |
|       |       |       | devel |
|       |       |       | oper' |
|       |       |       | s     |
|       |       |       | text  |
|       |       |       | edito |
|       |       |       | r     |
|       |       |       | that  |
|       |       |       | suppo |
|       |       |       | rts   |
|       |       |       | pytho |
|       |       |       | n     |
|       |       |       | synta |
|       |       |       | x     |
|       |       |       | highl |
|       |       |       | ighti |
|       |       |       | ng,   |
|       |       |       | auto- |
|       |       |       | inden |
|       |       |       | t,    |
|       |       |       | auto- |
|       |       |       | compl |
|       |       |       | etion |
|       |       |       | ,     |
|       |       |       | class |
|       |       |       | brows |
|       |       |       | er,   |
|       |       |       | and   |
|       |       |       | can   |
|       |       |       | run   |
|       |       |       | scrip |
|       |       |       | ts    |
|       |       |       | from  |
|       |       |       | insid |
|       |       |       | e     |
|       |       |       | the   |
|       |       |       | edito |
|       |       |       | r.    |
+-------+-------+-------+-------+
| Pytho | Windo | 2013  | Open- |
| n     | ws    |       | sourc |
| Tools |       |       | e     |
| for   |       |       | plugi |
| Visua |       |       | n     |
| l     |       |       | for   |
| Studi |       |       | Visua |
| o     |       |       | l     |
|       |       |       | Studi |
|       |       |       | o     |
|       |       |       | 2010, |
|       |       |       | 2012  |
|       |       |       | and   |
|       |       |       | 2013. |
|       |       |       | Suppo |
|       |       |       | rts   |
|       |       |       | synta |
|       |       |       | x     |
|       |       |       | highl |
|       |       |       | ighti |
|       |       |       | ng,   |
|       |       |       | debug |
|       |       |       | ging  |
|       |       |       | and   |
|       |       |       | rich  |
|       |       |       | intel |
|       |       |       | lisen |
|       |       |       | se,   |
|       |       |       | refac |
|       |       |       | torin |
|       |       |       | g,    |
|       |       |       | objec |
|       |       |       | t     |
|       |       |       | brows |
|       |       |       | er,   |
|       |       |       | MPI   |
|       |       |       | clust |
|       |       |       | er    |
|       |       |       | debug |
|       |       |       | ging, |
|       |       |       | Djang |
|       |       |       | o     |
|       |       |       | intel |
|       |       |       | lisen |
|       |       |       | se    |
|       |       |       | and   |
|       |       |       | debug |
|       |       |       | ging, |
|       |       |       | devel |
|       |       |       | opmen |
|       |       |       | t     |
|       |       |       | REPL  |
|       |       |       | windo |
|       |       |       | w     |
|       |       |       | and a |
|       |       |       | debug |
|       |       |       | ging  |
|       |       |       | REPL  |
|       |       |       | windo |
|       |       |       | w.    |
|       |       |       | Suppo |
|       |       |       | rts   |
|       |       |       | mixed |
|       |       |       | -mode |
|       |       |       | Pytho |
|       |       |       | n/C/C |
|       |       |       | ++    |
|       |       |       | debug |
|       |       |       | ging. |
+-------+-------+-------+-------+
| Exedo | Mac   | 2013  | Comme |
| re    | OS X  |       | rcial |
|       |       |       | with  |
|       |       |       | featu |
|       |       |       | re-li |
|       |       |       | mited |
|       |       |       | free  |
|       |       |       | trial |
|       |       |       | .     |
|       |       |       | A     |
|       |       |       | Mac-n |
|       |       |       | ative |
|       |       |       | ,     |
|       |       |       | singl |
|       |       |       | e-win |
|       |       |       | dow   |
|       |       |       | IDE   |
|       |       |       | inspi |
|       |       |       | red   |
|       |       |       | by    |
|       |       |       | Xcode |
|       |       |       | .     |
|       |       |       | Featu |
|       |       |       | res   |
|       |       |       | integ |
|       |       |       | rated |
|       |       |       | debug |
|       |       |       | ger,  |
|       |       |       | tabs, |
|       |       |       | code  |
|       |       |       | compl |
|       |       |       | etion |
|       |       |       | with  |
|       |       |       | tab   |
|       |       |       | trigg |
|       |       |       | ers,  |
|       |       |       | synta |
|       |       |       | x     |
|       |       |       | highl |
|       |       |       | ighti |
|       |       |       | ng    |
|       |       |       | theme |
|       |       |       | s,    |
|       |       |       | searc |
|       |       |       | h     |
|       |       |       | and   |
|       |       |       | repla |
|       |       |       | ce    |
|       |       |       | with  |
|       |       |       | regex |
|       |       |       | ,     |
|       |       |       | integ |
|       |       |       | rated |
|       |       |       | REPL  |
|       |       |       | sessi |
|       |       |       | ons,  |
|       |       |       | goto  |
|       |       |       | defin |
|       |       |       | ition |
|       |       |       | ,     |
|       |       |       | file  |
|       |       |       | brows |
|       |       |       | er,   |
|       |       |       | integ |
|       |       |       | rated |
|       |       |       | docum |
|       |       |       | entat |
|       |       |       | ion   |
|       |       |       | brows |
|       |       |       | er.   |
|       |       |       | As of |
|       |       |       | June  |
|       |       |       | 2015, |
|       |       |       | does  |
|       |       |       | not   |
|       |       |       | suppo |
|       |       |       | rt    |
|       |       |       | input |
|       |       |       | ()    |
|       |       |       | meani |
|       |       |       | ng    |
|       |       |       | any   |
|       |       |       | conso |
|       |       |       | le    |
|       |       |       | input |
|       |       |       | using |
|       |       |       | this  |
|       |       |       | funct |
|       |       |       | ion   |
|       |       |       | is    |
|       |       |       | not   |
|       |       |       | suppo |
|       |       |       | rted. |
+-------+-------+-------+-------+

There are also text editors specialized in programming code, which have
features like syntax colorization, export to other formats and convert
text encoding.

These editors support multiple programming languages​​, Python among
them:

-  `SciTE <http://www.scintilla.org/SciTE.html>`__
-  `Notepad++ <http://notepad-plus.sourceforge.net/br/site.htm>`__

**Shell** is the name given to interactive environments for executing
commands that can be used to test small pieces of code and for
activities like data crunching (extraction of information of interest in
masses of data and subsequent translation to other formats).

Beyond the standard Python **Shell**, there are others available:

-  PyCrust
-  IPython
-  Reinteract
-  bpython
-  PyroShell

**Packers** are utilities that are used to build executables that
comprise the bytecode, the interpreter and other dependencies, allowing
the application to run on machines without Python installed, which
facilitates program distribution.

Among packers for Python, are available:

-  py2exe (Windows only)
-  cx\_Freeze (portable)

**Frameworks** are collections of software components (libraries,
utilities and others) that have been designed to be used by other
systems.

Some of the most known *frameworks* availble are:

-  Web: Django, TurboGears, Zope and web2py.
-  Graphic interface: wxPython, PyGTK and PyQt.
-  Scientific processing: NumPy and SciPy.
-  Image processing: PIL.
-  2D: Matplotlib and SVGFig.
-  3D: Visual Python, PyOpenGL and Python Ogre.
-  Object-relational mapping: SQLAlchemy e SQLObject.

Culture
-------

The name Python was taken by Guido van Rossum from british TV program
*Monty Python's Flying Circus*, and there are many references to the
show in its documentation. For instance, Python's oficial package
repository was called Cheese Shop, the name of one of the frames of the
program. Currently, the repository name is `Python Package
Index <http://pypi.python.org/pypi>`__ (PYPI).

The goals of the project are summarized by Tim Peters in a text called
*Zen of Python*, which can be found in Python itself using the command:

.. code:: python

    import this

The Zen of Python
-----------------

-  Beautiful is better than ugly.
-  Explicit is better than implicit.
-  Simple is better than complex.
-  Complex is better than complicated.
-  Flat is better than nested.
-  Sparse is better than dense.
-  Readability counts.
-  Special cases aren''t special enough to break the rules.
-  Although practicality beats purity.
-  Errors should never pass silently.
-  Unless explicitly silenced.
-  In the face of ambiguity, refuse the temptation to guess.
-  There should be one -- and preferably only one -- obvious way to do
   it.
-  Although that way may not be obvious at first unless you're Dutch.
-  Now is better than never.
-  Although never is often better than *right* now.
-  If the implementation is hard to explain, it's a bad idea.
-  If the implementation is easy to explain, it may be a good idea.
-  Namespaces are one honking great idea -- let's do more of those!
