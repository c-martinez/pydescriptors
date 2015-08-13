# Compactness measures

The compactness package contains Python implementation of various 2D and 3D compactness measures described in [2D and 3D Shape Descriptors](http://hdl.handle.net/10036/3026).

## Installation

You can install this package by downloading the source and installing it with pip:
```
$ wget https://github.com/c-martinez/compactness/archive/master.zip
$ pip install master.zip
```

Or directly from git:
```
$ pip install git+git://github.com/c-martinez/compactness.git
```

## Usage
```
from compactness.compactness import compactness_hz,compactness_bribiesca
from compactness.helpers import getSphere

sphere = getSphere(20)
X,Y,Z = sphere.nonzero()

compactness_bribiesca(X,Y,Z)
compactness_hz(X,Y,Z)
```

## Dependencies
 - Numpy

## Testing
Run:

```
$ nosetests
```

## Citations
If you use this code, please cite [2D and 3D Shape Descriptors](http://hdl.handle.net/10036/3026).


TODO:
 - Rename package
 - Add tests for compactness
 - Add Usage
 - Add installation guide (from source)
 - Add more descriptors
 - Documentation
 - Auto testing
 - pyflakes (auto)
 - pep8 (auto)
