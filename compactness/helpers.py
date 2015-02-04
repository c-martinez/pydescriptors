import numpy as np

def getSphere(side):
    volume = np.zeros((side,side,side))
    r = side/2
    Xs,Ys = np.meshgrid(np.arange(-r,r), np.arange(-r,r))
    for k,z in enumerate(np.arange(-r,r)):
        volume[:,:,k] = np.sqrt(Xs**2 + Ys**2 + z**2)<r
    return volume

def rotate3D(X,Y,Z,rx,ry):
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
