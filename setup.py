"""
pyframe

Simple command line tool to simplify
package framework configuration.
"""

__author__ = 'neolytics'
from setuptools import setup, find_packages
from pyframe import __version__

setup(
    name='pyframe',
    version=__version__,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pyframe = pyframe.__main__:run",
        ]
    },
    license='',
    author='Jon Staples',
    description='Happy little python package framework util.'
)
