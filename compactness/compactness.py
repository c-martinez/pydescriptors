import numpy as np

def int_max_abs(X,Y,Z):
    # X, Y, Z must be centred
    XYZ = np.vstack([ X,Y,Z ])
    max_abs = np.absolute(XYZ).max(axis=0)
    sss = max_abs.sum()
    return sss
