from setuptools import setup, find_packages

VERSION = '0.1.6'

setup(
    name='ztdebugger',  # package name
    version=VERSION,  # package version
    description='my custom debugger',  # package description
    packages=find_packages(),
    zip_safe=False,
    long_description="Detail description can be found at https://github.com/zhou6140919/debugger",
    install_requires=[
        'rich',
        'pysnooper',
        'icecream',
        'q',
    ],
)
