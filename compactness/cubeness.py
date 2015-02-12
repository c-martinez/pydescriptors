from __future__ import division

import numpy as np
from moments import immoment3D
from helpers import rotate3D

def __int_max_abs__(X,Y,Z):
    # \sss max(|x|,|y|,|z|) dx dy dz
    # X, Y, Z must be centred
    XYZ = np.vstack([ X,Y,Z ])
    max_abs = np.absolute(XYZ).max(axis=0)
    sss = max_abs.sum()
    return sss

def cubeness_mz(X,Y,Z,nSteps=100):
    m000 = immoment3D(X,Y,Z,0,0,0)
    m100 = immoment3D(X,Y,Z,1,0,0)
    m010 = immoment3D(X,Y,Z,0,1,0)
    m001 = immoment3D(X,Y,Z,0,0,1)

    # Find centroid
    cx = m100/m000
    cy = m010/m000
    cz = m001/m000

    # Recentering (because it doesn't hurt)
    X_ = X - cx
    Y_ = Y - cy
    Z_ = Z - cz
    
    # TODO: assert centorid is close to 0,0,0 ?

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
    return c,fxy

