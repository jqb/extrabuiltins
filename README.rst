extrabuiltins
*************

Simple package that gives ability to extend __builtin__ temporarily.

Usage::
   >>> from extrabuiltins import extrabuiltins
   >>>
   >>> with extrabuiltins({'hello': lambda : "Hello!"}):
   >>>     print hello()  # hello available as builtin
   >>>
   >>> hello!


Installation
------------

simply download and install::

  python setup.py install

or directly from github::

  pip install -e git+git@github.com:jqb/extrabuiltins.git#egg=extrabuiltins
