from compactness.cubeness import cubeness_mz
from compactness.helpers import getSphere

import numpy as np

from numpy.testing import assert_almost_equal

def test_cubenessMZ_cube():
    volume = np.ones((50,50,50))
    X,Y,Z = volume.nonzero()

    c,fxy = cubeness_mz(X,Y,Z)

    # More precision requires more computation -- for unit test this is enough
    assert_almost_equal(c,1.000,2)

def test_cubenessMZ_sphere():
    volume = getSphere(50)
    X,Y,Z = volume.nonzero()

    c,fxy = cubeness_mz(X,Y,Z)

    # More precision requires more computation -- for unit test this is enough
    assert_almost_equal(c,0.971,2)
