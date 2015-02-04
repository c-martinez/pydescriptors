def immoment3D(X,Y,Z,p,q,r):
    # TODO: 
    # Occupacy matrix not supported
    # If we need central moments: 
    # Xc,Yc,Zc = m100 / m000, m010 / m000, m001 / m000
    # return ((X-Xc)**p * (Y-Yc)**q * (Z-Zc)**r).sum()
    return (X**p * Y**q * Z**r).sum()
