from setuptools import setup, find_packages

from travis_example import __version__

setup(
    name = 'travis example',
    version = __version__,
    packages = find_packages(),    
)
