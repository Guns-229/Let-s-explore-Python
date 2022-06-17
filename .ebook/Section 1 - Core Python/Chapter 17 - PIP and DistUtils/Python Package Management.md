
# Python Package Management

The Python libraries are distributed using following methods:

- `distutils` packages
    - python `setup.py`
    - Python `Eggs`
    - Python Wheel files `whl`
- Package managers such as dpkg, rpm, msi, etc

## distutils

One of the most popular method to distribute the python packages is using `distutils`.
The package is distributed in compressed format (such as `tar.gz`, `tar.bz2` and `.zip`).

End users extract the compressed files and run the following command to install the package. 

```
python setup.py install
```
which results in package getting installed in "site-packages" folder of Python installation.

### Creating distribution

We are going to use dummy python app and call it `mayadiff`. Steps to create the distribution package for the app are as follows:

#### Step 1: Create Folder Structure

Lets create the following folders. Just replace <`mayadiff`> to your app name. 

```
/mayadiff/
    /mayadiff
```

#### Step 2: Create `__init__.py` file

create `__init__.py` file as shown below
```
/mayadiff/
    /mayadiff
    __init__.py
```
Also, add the following code to the file
```python
name = "mayadiff"
```

#### Step 3: Creating package files

The following three files, provides all the information needed for the application to be packaged. 

- `setup.py`
- `LICENSE`
- `README.md`

If you have files other than python scripts, then you might wish to create `MANIFEST.in` file and populate is as shown below
```
include mayadiff/doc/*.*
include mayadiff/opt.conf
include mayadiff/report_files/*
include mayadiff/report_files/css/*.*
include mayadiff/report_files/images/*.*
include mayadiff/report_files/js/*.*
```
Also add `include_package_data=True` option in `setup.py` file 

`setup.py` is the `build` script, which cotains all the logic and details to compile (if needed) and deploy the app on the machine. 

The sample `setup.py` is shown below. You can update it as per your requirement.

```python
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mayadiff",
    version="0.0.2",  # check PEP: 440
    author="Mayank Johri",
    author_email="mayankjohri@gmail.com",
    description="An Application to create a diff between two folders/files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://sourceforge.net/projects/pyfoldercompare",
    include_package_data=True,
    packages=setuptools.find_packages(),
    scripts=["mayadiff/cmpfiles.py", "mayadiff/img_cmp.py", "mayadiff/slate.py"],
    package_data={
        "doc": ["mayadiff/doc/*"],
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU 3 License",
        "Operating System :: OS Independent",
    ],
)

```

`LICENSE` file should contain the license under which the application is to be distributed. For open source applications/libraries, check https://choosealicense.com/ link for help picking a license.

I normally use either `AGNU` or `GNU3.0`, but you can choose one which suits your requirement.

#### Copy application/library files 

copy the required files in inner `mayadiff` folder.

#### Create distribution package

Before creating the distribution package, we need to make sure we have latest version of `setuptools` and `wheel` installed
```
python3 -m pip install --user --upgrade setuptools wheel
```
Now lets run the following command to create the package. (_Please run the below command where setup.py file is located._)
```
python3 setup.py sdist bdist_wheel
```
The above command will create two files `.whl` and `tar.gz` in `dist` folder. 
```
$:\> ls dist
mayadiff-0.0.2-py3-none-any.whl  mayadiff-0.0.2.tar.gz
```

#### Testing and Distribution

Now, the created `.whl` file can be tested by using `pip` to install and later uploaded to pypi.org website.

## Package managers such as dpkg, rpm, msi

Package managers from operating System usually work with their own packet formats, like ".deb" (Debian Linux) or ".rpm" (RedHat Linux). How to install the packages depends on the manager. The big advantage is that the package manager takes care of dependencies and updates.

Installer programs are nothing more than executables that install the library. They are generally used in Windows environments and can be uninstalled from the Control Panel.
