from setuptools import setup

_major = 0
_minor = 1
_revision = 2

_version = "%d.%d.%d" % (_major, _minor, _revision)

setup(
    name="pydescriptors",
    description="Implementation of various 2D and 3D compactness measures " +
                "described in 2D and 3D Shape Descriptors.",
    url="https://github.com/c-martinez/compactness",
    version=_version,
    packages=["pydescriptors"],
    package_dir={"pydescriptors": "pydescriptors"},
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Image processing",
    ],
    install_requires=['numpy']
)

