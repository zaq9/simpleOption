from setuptools import setup
setup(
    name='simpleOption',
    version='0.1.1',
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
    ],
    keywords=['options','python','finance'],
    install_requires=['parse','quantlib-python'],
)
