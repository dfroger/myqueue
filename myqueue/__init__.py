#!/usr/bin/env python

VERSION = (0, 1, '0')
__version__ = '.'.join(str(v) for v in VERSION)
__version_full__ = __version__

from .mystack import MyStack
from .myqueue import MyQueue
from .error import Empty
