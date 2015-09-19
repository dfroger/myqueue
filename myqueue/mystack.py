#!/usr/bin/env python

class MyStack:
    def __init__(self):
        self._size = 0

    @property
    def size(self):
        return self._size

    def add(self, item):
        self._size += 1

    def peek(self):
        self._size -= 1
