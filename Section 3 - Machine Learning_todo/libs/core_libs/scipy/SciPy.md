
# SciPy
----

SciPy is a collection of mathematical algorithms and convenience functions built on the Numpy extension of Python. It adds significant power to the interactive Python session by providing the user with high-level commands and classes for manipulating and visualizing data. With SciPy an interactive Python session becomes a data-processing and system-prototyping environment rivaling systems such as MATLAB, IDL, Octave, R-Lab, and SciLab.

The additional benefit of basing SciPy on Python is that this also makes a powerful programming language available for use in developing sophisticated programs and specialized applications. Scientific applications using SciPy benefit from the development of additional modules in numerous niches of the software landscape by developers across the world. Everything from parallel programming to web and data-base subroutines and classes have been made available to the Python programmer. All of this power is available in addition to the mathematical libraries in SciPy.


```python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
```

## SciPy Organization

| Subpackage  	| Description                                            	|
|-------------	|--------------------------------------------------------	|
| cluster     	| Clustering algorithms                                  	|
| constants   	| Physical and mathematical constants                    	|
| fftpack     	| Fast Fourier Transform routines                        	|
| integrate   	| Integration and ordinary differential equation solvers 	|
| interpolate 	| Interpolation and smoothing splines                    	|
| io          	| Input and Output                                       	|
| linalg      	| Linear algebra                                         	|
| ndimage     	| N-dimensional image processing                         	|
| odr         	| Orthogonal distance regression                         	|
| optimize    	| Optimization and root-finding routines                 	|
| signal      	| Signal processing                                      	|
| sparse      	| Sparse matrices and associated routines                	|
| spatial     	| Spatial data structures and algorithms                 	|
| special     	| Special functions                                      	|
| stats       	| Statistical distributions and functions                	|

## Relationship with numpy
As Scipy builds on Numpy, it uses it for all basic array handling requirements. Although scipy also contains functions from numpy and numpy.lib.scimath, but it is better to use them directly from the numpy module.

### Index Tricks


```python
np.arange(-1, 1.002, 2/9.0)
```




    array([-1.        , -0.77777778, -0.55555556, -0.33333333, -0.11111111,
            0.11111111,  0.33333333,  0.55555556,  0.77777778,  1.        ])




```python
a = np.concatenate(([3], [0]*5, np.arange(-1, 1.002, 2/9.0)))
print(a)
```

    [ 3.          0.          0.          0.          0.          0.         -1.
     -0.77777778 -0.55555556 -0.33333333 -0.11111111  0.11111111  0.33333333
      0.55555556  0.77777778  1.        ]



```python
a = np.r_[3,[0]*5,-1:1:10j]
print(a)
```

    [ 3.          0.          0.          0.          0.          0.         -1.
     -0.77777778 -0.55555556 -0.33333333 -0.11111111  0.11111111  0.33333333
      0.55555556  0.77777778  1.        ]


### Shape manipulation

 functions are routines for squeezing out length- one dimensions from N-dimensional arrays, ensuring that an array is at least 1-, 2-, or 3-dimensional, and stacking (concatenating) arrays by rows, columns, and “pages “(in the third dimension). Routines for splitting arrays (roughly the opposite of stacking arrays) are also available.

#### Polynomials

There are two (interchangeable) ways to deal with 1-d polynomials in SciPy. The first is to use the poly1d class from Numpy. This class accepts coefficients or polynomial roots to initialize a polynomial. The polynomial object can then be manipulated in algebraic expressions, integrated, differentiated, and evaluated. It even prints like a polynomial:


```python
from numpy import poly1d
```


```python
p = poly1d([3,4,5])
print(p)
```

       2
    3 x + 4 x + 5
       4      3      2
    9 x + 24 x + 46 x + 40 x + 25



```python
print(p*p)
```

       4      3      2
    9 x + 24 x + 46 x + 40 x + 25



```python
print(p.integ(k=6))
```

       3     2
    1 x + 2 x + 5 x + 6


The other way to handle polynomials is as an array of coefficients with the first element of the array giving the coefficient of the highest power. There are explicit functions to add, subtract, multiply, divide, integrate, differentiate, and evaluate polynomials represented as sequences of coefficients.

#### Vectorizing functions (vectorize)


```python


```
