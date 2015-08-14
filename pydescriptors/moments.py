def immoment3D(X, Y, Z, p, q, r):
    """Compute the P,Q,R moments of a 3D image.

    Keyword arguments:
    X -- The X coordinates of voxels
    Y -- The Y coordinates of voxels
    Z -- The Z coordinates of voxels
    P -- The power used for the X-axis
    Q -- The power used for the Y-axis
    R -- The power used for the Z-axis

    Returns:
    The numeric value of the PQR moment.
    """
    assert len(X) == len(Y)
    assert len(Y) == len(Z)
    return (X ** p * Y ** q * Z ** r).sum()
