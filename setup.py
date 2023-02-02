from setuptools import setup, find_packages


VERSION = '0.1.0'

setup(
    name='debugger',  # package name
    version=VERSION,  # package version
    description='my debugger',  # package description
    packages=find_packages(),
    zip_safe=False,
)
