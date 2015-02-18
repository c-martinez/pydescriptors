import numpy as np

from moments import immoment3D

def getSphere(side):
    """Create a 3D volume of sideXsideXside, where voxels representing a 
    sphere are ones and background is zeros.

    Keyword arguments:
    side -- the number of voxels the 3D volume should have on each side.

    Returns:
    A (side,side,side) shaped matrix of zeros and ones.
    """
    volume = np.zeros((side,side,side))
    r = side/2
    Xs,Ys = np.meshgrid(np.arange(-r,r), np.arange(-r,r))
    for k,z in enumerate(np.arange(-r,r)):
        volume[:,:,k] = np.sqrt(Xs**2 + Ys**2 + z**2)<r
    return volume

def rotate3D(X,Y,Z,rx,ry):
    """Rotates a 3D object along one ordinate axis at a time.

    Keyword arguments:
    X -- The X coordinate of the voxels to be rotated.
    Y -- The Y coordinate of the voxels to be rotated.
    Z -- The Z coordinate of the voxels to be rotated.

    Returns:
    X,Y,Z coordinates of the rotated voxels.
    """
    R = np.eye(3)
    Rx = np.array([[ 1, 0, 0],
       [ 0, np.cos(rx), -np.sin(rx) ],
       [ 0, np.sin(rx),  np.cos(rx) ]])
    Ry = np.array([[ np.cos(ry), 0, np.sin(ry) ],
       [ 0, 1, 0 ],
       [ -np.sin(ry), 0, np.cos(ry) ]])
    R = np.dot(R,Rx)
    R = np.dot(R,Ry)

    XYZ = np.vstack([ X,Y,Z ])
    XYZ_ = np.dot(XYZ.T, R)

    return XYZ_[:,0],XYZ_[:,1],XYZ_[:,2]

def recenter(X,Y,Z):
    # TODO: Document, write unit test
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

    return X_,Y_,Z_
