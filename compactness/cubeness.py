from __future__ import division

import numpy as np
# from numpy.testing import assert_almost_equal
from moments import immoment3D
from helpers import rotate3D

def __int_max_abs__(X,Y,Z):
    """Calculate the triple integral maximum absolute value of a given 3D object.

    Keyword arguments:
    X -- The X coordinate of the voxels.
    Y -- The Y coordinate of the voxels.
    Z -- The Z coordinate of the voxels.

    Returns:
    The value of the integral.
    """
    # \iiint max(|x|,|y|,|z|) dx dy dz
    # X, Y, Z must be centred
    XYZ = np.vstack([ X,Y,Z ])
    max_abs = np.absolute(XYZ).max(axis=0)
    sss = max_abs.sum()
    return sss

def cubeness_mz(X,Y,Z,nSteps=100):
    """Computes the cubeness of a 3D object by method presented in
    paper: Measuring Cubeness of 3D Shapes by Martinez-Ortiz and Zunic.

    Keyword arguments:
    X -- The X coordinate of the voxels.
    Y -- The Y coordinate of the voxels.
    Z -- The Z coordinate of the voxels.

    Returns:
    c -- The cubeness_mz value of the given object.
    """
    m000 = immoment3D(X,Y,Z,0,0,0)
    m100 = immoment3D(X,Y,Z,1,0,0)
    m010 = immoment3D(X,Y,Z,0,1,0)
    m001 = immoment3D(X,Y,Z,0,0,1)

    # Find centroid
    cx = m100/m000
    cy = m010/m000
    cz = m001/m000

    # Recentering
    X_ = X - cx
    Y_ = Y - cy
    Z_ = Z - cz
    
    # TODO: assert centorid is close to 0,0,0 ?
    # assert_almost_equal(immoment3D(X_,Y_,Z_,1,0,0),0,4) # X
    # assert_almost_equal(immoment3D(X_,Y_,Z_,0,1,0),0,4) # Y
    # assert_almost_equal(immoment3D(X_,Y_,Z_,0,0,1),0,4) # Z

    angles = np.linspace(0,np.pi,nSteps)
    fxy = np.zeros((nSteps,nSteps))
    # TODO: Pythonize these for loops (at the cost of readability?)
    for i,rx in enumerate(angles):
        for j,ry in enumerate(angles):
            Xr,Yr,Zr = rotate3D(X_,Y_,Z_,rx,ry)
            fxy[i,j] = __int_max_abs__(Xr,Yr,Zr)

    vol = m000
    min_fxy = fxy.min()
    c = (3/8) * vol**(4/3) / min_fxy
    return c

def cubeness_fit():
    pass
