#!/usr/bin/env python

VERSION = (0, 1, 'dev0')
__version__ = '.'.join(str(v) for v in VERSION)
__version_full__ = __version__

from .myqueue import MyQueue