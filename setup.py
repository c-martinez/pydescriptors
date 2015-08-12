from setuptools import setup

setup(
    name="compactness",
    description="Implementation of various 2D and 3D compactness measures described in 2D and 3D Shape Descriptors.",
    url="https://github.com/c-martinez/compactness",
    version="0.0.1",
    packages=["compactness"],
    package_dir={"compactness": "compactness"},
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Image processing",
    ],
    install_requires=[]
)
