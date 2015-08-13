from compactness.moments import immoment3D
from compactness.helpers import getSphere


def test_moment000():
    """Test the 0-th order moment. For any given shape, this should be the same
    as the volume of the object.
    """
    volume = getSphere(50)
    X, Y, Z = volume.nonzero()

    # Moment 0,0,0 is the volume of the object
    assert volume.sum() == immoment3D(X, Y, Z, 0, 0, 0)
    assert len(X) == immoment3D(X, Y, Z, 0, 0, 0)


def test_recentering():
    """Test calculating the centroid of an object.
    """
    volume = getSphere(50)
    X, Y, Z = volume.nonzero()

    m000 = immoment3D(X, Y, Z, 0, 0, 0)
    m100 = immoment3D(X, Y, Z, 1, 0, 0)
    m010 = immoment3D(X, Y, Z, 0, 1, 0)
    m001 = immoment3D(X, Y, Z, 0, 0, 1)

    # recentering
    X = X - (m100 / m000)
    Y = Y - (m010 / m000)
    Z = Z - (m001 / m000)

    # After recentering, object should be located at 0,0,0
    assert immoment3D(X, Y, Z, 1, 0, 0) == 0
    assert immoment3D(X, Y, Z, 0, 1, 0) == 0
    assert immoment3D(X, Y, Z, 0, 0, 1) == 0
