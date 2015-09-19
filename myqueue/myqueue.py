#!/usr/bin/env python

from .mystack import MyStack
from .error import Empty

class MyQueue:
    def __init__(self):
        self._size = 0
        self._incoming = MyStack()
        self._outgoing = MyStack()

    @property
    def size(self):
        return self._size

    def add(self, item):
        self._incoming.add(item)
        self._size += 1

    def peek(self):
        if not self._outgoing.size:
            if self._incoming.size:
                self._decant_incoming_into_outgoing()
            else:
                raise Empty("Can't peek item from empty queue")
        item = self._outgoing.peek()
        self._size -= 1
        return item

    def _decant_incoming_into_outgoing(self):
        while self._incoming.size:
            item = self._incoming.peek()
            self._outgoing.add(item)
