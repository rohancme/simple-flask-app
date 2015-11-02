"""Based on https://github.com/pypa/sampleproject/blob/master/setup.py."""

from setuptools import setup, find_packages

setup(
    name='party-gifs',
    version='0.1.0',
    author='rohan chakravarthy',
    author_email='rchakra3@ncsu.edu',
    license='GNU GPLv2',
    # The project's main homepage
    url='https://github.com/rchakra3/simple-flask-app',
    packages=find_packages(exclude=('tests*')),
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    include_package_data=True,
    zip_safe=False
)
