# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='extrabuiltins',
    version='1.0',
    description='Simple package that gives ability to extend __builtin__ temporarily.',
    author='Kuba Janoszek',
    author_email='kuba.janoszek@gmail.com',
    url='http://github.com/jqb/extrabuiltins/tree/master',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    setup_requires=['setuptools_git'],
    zip_safe=False,
)

