# -*- coding: utf-8 -*-
from contextlib import contextmanager


@contextmanager
def extrabuiltins(things):
    """Simple context manager that gives ability to extend
    __builtin__'s temporarily.

    :param things: the dictionary with external builtin's
    :type things: dict

    Usage:
    >>> from extrabuiltins import extrabuiltins
    >>>
    >>> with extrabuiltins({'hello': lambda : "Hello!"}):
    >>>     print hello()  # hello available as builtin
    >>>
    >>> hello!
    """
    import __builtin__
    try:
        for name, thing in things.iteritems():
            setattr(__builtin__, name, thing)
        yield
    finally:
        for name in things:
            delattr(__builtin__, name)
