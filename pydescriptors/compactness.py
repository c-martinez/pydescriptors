from __future__ import division

from moments import immoment3D as _immoment3D
from helpers import recenter as _recenter

import numpy as _np


def bribiesca(X, Y, Z):
    assert X.shape[0] == Y.shape[0]
    assert Y.shape[0] == Z.shape[0]

    n = X.shape[0]
    A = _findArea(X, Y, Z)
    c = (n - (A / 6)) / (n - n ** (2 / 3))
    return c


def _findArea(X, Y, Z):
    voxels = set()
    for x, y, z in zip(X, Y, Z):
        voxels.add((x, y, z))

    neighbours = [_np.array([-1, 0, 0]), _np.array([1, 0, 0]),
                  _np.array([0, -1, 0]), _np.array([0, 1, 0]),
                  _np.array([0, 0, -1]), _np.array([0, 0, 1])]
    A = 0
    # For each voxel
    for x, y, z in zip(X, Y, Z):
        # Check its 6 possible neighbours
        vox = _np.asarray(x, y, z)
        for neigh in neighbours:
            vNeigh = vox + neigh
            # If neighbour is there, contribute 0 area
            # Otherwise, contribute 1
            A += 0 if tuple(vNeigh) in voxels else 1
    return A


def hz(X, Y, Z):
    X_, Y_, Z_ = _recenter(X, Y, Z)

    mu000 = _immoment3D(X_, Y_, Z_, 0, 0, 0)
    mu200 = _immoment3D(X_, Y_, Z_, 2, 0, 0)
    mu020 = _immoment3D(X_, Y_, Z_, 0, 2, 0)
    mu002 = _immoment3D(X_, Y_, Z_, 0, 0, 2)

    c = 3 ** (5 / 3) / (5 * ((4 * _np.pi) ** (2 / 3))) * \
        (mu000 ** (5 / 3) / (mu200 + mu020 + mu002))
    return c


def hzweighted(X, Y, Z, beta):
    X_, Y_, Z_ = _recenter(X, Y, Z)

    mu000 = _immoment3D(X_, Y_, Z_, 0, 0, 0)

    # int int int ( x^2 + y^2 +z^2 ) ^ beta dx dy dz
    tri_integral = _triintegral(X_, Y_, Z_, beta)

    if beta >= 0:
        # c = (3 / ( 2 * beta + 3)) * ...
        #     (( 3 / (4 * pi)) ^ ((2 * beta) / 3)) * ...
        #     ((mu000 ^ ((2*beta + 3) / 3)) / tri_integral);
        const1 = 3 / (2 * beta + 3)
        const2 = (3 / (4 * _np.pi)) ** ((2 * beta) / 3)
        numera = mu000 ** ((2 * beta + 3) / 3)
        divis = tri_integral
    elif -1.5 < beta and beta < 0:
        # c = ( ( 2 * beta + 3) / 3 ) * ...
        #     ( ( (4 * pi) / 3 ) ^ ( (2 * beta) / 3)) * ...
        #     ( tri_integral / ( mu000 ^ ((2 * beta + 3) / 3) ) );
        const1 = (2 * beta + 3) / 3
        const2 = ((4 * _np.pi) / 3) ** ((2 * beta) / 3)
        numera = tri_integral
        divis = mu000 ** ((2 * beta + 3) / 3)
    else:
        const1 = const2 = numera = 0
        divis = 1

    c = const1 * const2 * (numera / divis)
    return c


def _triintegral(X_, Y_, Z_, beta):
    xyz_beta = (X_ ** 2 + Y_ ** 2 + Z_ ** 2) ** beta
    return xyz_beta.sum()
