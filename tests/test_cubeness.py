from pydescriptors.cubeness import mz as cubeness_mz
from pydescriptors.cubeness import fit as cubeness_fit
from pydescriptors.helpers import getSphere

import numpy as np

from numpy.testing import assert_almost_equal

_testDiameter = 10

def test_cubenessMZ_cube():
    """Test the cubeness_mz of a cube.
    """
    volume = np.ones((_testDiameter, _testDiameter, _testDiameter))
    X, Y, Z = volume.nonzero()

    c = cubeness_mz(X, Y, Z)

    # More precision requires more computation -- for unit test this is enough
    assert_almost_equal(c, 1.000, 2)


def test_cubenessMZ_sphere():
    """Test the cubeness_mz of a sphere.
    """
    volume = getSphere(_testDiameter)
    X, Y, Z = volume.nonzero()

    c = cubeness_mz(X, Y, Z)

    # More precision requires more computation -- for unit test this is enough
    assert_almost_equal(c, 0.971, 2)


def test_cubenessFit_cube():
    """Test the cubeness_fit of a cube.
    """
    volume = np.ones((_testDiameter, _testDiameter, _testDiameter))
    X, Y, Z = volume.nonzero()

    c = cubeness_fit(X, Y, Z)

    # More precision requires more computation -- for unit test this is enough
    assert_almost_equal(c, 1.000, 2)


def test_cubenessFit_sphere():
    """Test the cubeness_fit of a sphere.
    """
    volume = getSphere(_testDiameter)
    X, Y, Z = volume.nonzero()

    c = cubeness_fit(X, Y, Z)

    # More precision requires more computation -- for unit test this is enough
    assert_almost_equal(c, 0.723, 2)


def xtest_cubenessMZ_beta_cube():
    assert 1==0, "Not yet implemented"


def xtest_cubenessMZ_beta_sphere():
    assert 1==0, "Not yet implemented"
