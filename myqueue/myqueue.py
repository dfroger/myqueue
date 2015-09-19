#!/usr/bin/env python

class MyQueue:
    def __init__(self):
        self._size = 0

    @property
    def size(self):
        return self._size
