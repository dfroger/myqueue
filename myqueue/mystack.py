#!/usr/bin/env python

class MyStack:
    def __init__(self):
        self._size = 0
        self._items = []

    @property
    def size(self):
        return self._size

    def add(self, item):
        self._size += 1
        self._items.append(item)

    def peek(self):
        item = self._items.pop()
        self._size -= 1
        return item
