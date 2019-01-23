from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))


setup(
    name='simpleOption',
    version='0.1.3',
    description='Simple Option module(using QuantLib)',
    url='https://github.com/zaq9/simpleOption',
    author='zaq',
    author_email='zaq_9@yahoo.co.jp',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
    ],
    keywords=['options','python','finance'],
    py_modules=["my_module"],
    #packages=find_packages(exclude=['contrib', 'docs', 'tests']), 
    install_requires=['parse','quantlib-python'],
)
