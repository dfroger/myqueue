#!/usr/bin/env python

from .mystack import MyStack

class MyQueue:
    def __init__(self):
        self._size = 0
        self._incoming = MyStack()

    @property
    def size(self):
        return self._size

    def add(self, item):
        self._size += 1

    def peek(self):
        self._size -= 1
