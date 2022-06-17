
Chapter 12 : Third Party Libraries
=============================
_____________________________
There are many libraries written by others available for Python, consisting of packages or modules, that implement many features beyond the standard library.

Generally, the libraries are distributed in the following ways:

+ *distutils* packages.
+ Package managers from operating system.
+ Installers.
+ Python Eggs.

Packages using *distutils* module, which is distributed with Python, are very popular. The packages are distributed in compressed files (usually ".tar.gz" , ".tar.bz2" or ".zip " ). To install, you must unzip the file, go into the folder that was unzipped, and to execute the command:

    python setup.py install

The package will be installed in "site-packages" folder in Python.

Package managers from operating System usually work with their own packet formats, like ".deb" (Debian Linux) or ".rpm" (RedHat Linux). How to install the packages depends on the manager. The big advantage is that the package manager takes care of dependencies and updates.

Installer programs are nothing more than executables that install the library. They are generally used in Windows environments and can be uninstalled from the Control Panel.

Egg is a Python package format (with the extension ".egg") which is administered by the easy_install utility, which is part of the project [setuptools](http://peak.telecommunity.com/DevCenter/setuptools/). Similar to some tools found in other languages such as Ruby Gems, it is gradually becoming the de facto standard for distributing libraries in Python.

The program finds the newest version of the package in [PYPI](http://pypi.python.org/pypi) (*Python Package Index*), the Python package repository, and also tries to install dependencies as needed.

Python Egg packages can be installed via the command:

> easy_install package_name

The easy_install *script* is installed in the "scripts" folder of Python.
