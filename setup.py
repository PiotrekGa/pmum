#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name='pmum',
    author='Piotr Gabryś',
    author_email='piotrek.gabrys@gmail.com',
    description="Package for visualization of model's errors",
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.19.5',
        'pandas>=1.2.0',
        'scikit-learn>=0.24.0',
        'matplotlib>=3.3.3',
        'seaborn>=0.11.1'],
    extras_require={
        'dev': [
            'pytest>=6.3.1'
        ]
    },
    license='MIT',
    long_description=open('README.md').read(),
    url="https://github.com/PiotrekGa/pmum"
)
