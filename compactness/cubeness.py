from __future__ import division

import numpy as np
# from numpy.testing import assert_almost_equal
from moments import immoment3D
from helpers import rotate3D, recenter

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

def __int_max_abs_beta__(X,Y,Z,beta):
    """.
    """
    # \iiint max(|x|,|y|,|z|) dx dy dz
    # X, Y, Z must be centred
    XYZ = np.vstack([ X,Y,Z ]).astype(np.double)
    max_abs = np.absolute(XYZ).max(axis=0)
    max_abs_beta = max_abs[max_abs.nonzero()]**beta
    
    sss = max_abs_beta.sum()
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
    X_,Y_,Z_ = recenter(X,Y,Z)

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

    vol = immoment3D(X,Y,Z,0,0,0)
    min_fxy = fxy.min()
    c = (3/8) * vol**(4/3) / min_fxy
    return c

def cubeness_fit(X,Y,Z,nSteps=100):
    X_,Y_,Z_ = recenter(X,Y,Z)

    # Create fit cube of same volume as object
    vol_s = immoment3D(X,Y,Z,0,0,0)
    a_s_2 = np.round(vol_s**(1/3))  # Side of cube with equivalent volume
    b = np.ones((a_s_2,a_s_2,a_s_2))

    bX,bY,bZ = b.nonzero()
    bX,bY,bZ = recenter(bX,bY,bZ)

    XYZ_set = set([ (x,y,z) for x,y,z in zip(X_,Y_,Z_) ])

    angles = np.linspace(0,np.pi,nSteps)
    fxy = np.zeros((nSteps,nSteps))
    # TODO: Pythonize these for loops (at the cost of readability?)
    for i,rx in enumerate(angles):
        for j,ry in enumerate(angles):
            bXr,bYr,bZr = rotate3D(bX,bY,bZ,rx,ry)
            bXr = np.floor(bXr)
            bYr = np.floor(bYr)
            bZr = np.floor(bZr)

            br_set = set([ (x,y,z) for x,y,z in zip(bXr,bYr,bZr) ])

            uXYZ = br_set.union(XYZ_set)
            iXYZ = br_set.intersection(XYZ_set)

            uXYZ = np.array([ np.array([x,y,z]) for x,y,z in uXYZ ])
            iXYZ = np.array([ np.array([x,y,z]) for x,y,z in iXYZ ])

            vol_u = immoment3D(uXYZ[:,0],uXYZ[:,1],uXYZ[:,2],0,0,0)
            vol_i = immoment3D(iXYZ[:,0],iXYZ[:,1],iXYZ[:,2],0,0,0)

            fxy[i,j] = vol_i / vol_u

    c = fxy.max()
    return c

def cubeness_mz_beta(X,Y,Z,beta,nSteps=100):
    assert(beta>-3)
    X_,Y_,Z_ = recenter(X,Y,Z)
    
    angles = np.linspace(0,np.pi,nSteps)
    fxy = np.zeros((nSteps,nSteps))
    # TODO: Pythonize these for loops (at the cost of readability?)
    for i,rx in enumerate(angles):
        for j,ry in enumerate(angles):
            Xr,Yr,Zr = rotate3D(X_,Y_,Z_,rx,ry)
            fxy[i,j] = __int_max_abs_beta__(Xr,Yr,Zr,beta)

    vol = immoment3D(X,Y,Z,0,0,0)
    if beta>=0:
        c =   3/((2**beta) * (beta+3)) * vol**((beta+3)/3) / fxy.min()
    else:
        c =   ((2**beta) * (beta+3))/3 * fxy.min()   / vol**((beta+3)/3)
    return c

