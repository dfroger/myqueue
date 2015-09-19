#!/usr/bin/env python
"""
Implement a queue data structure.

The :mod:`myqueue.queue` module provide one class:

* :class:`MyQueue`: queue data structure.

"""


from .mystack import MyStack
from .error import Empty

class MyQueue:
    """
    A queue data structure.
    
    Items are added at the top and peeked from bottom

    For example:

        - Create empty queue.
        - Add items 42 and 43. 
        - Peek these items.

    ::

           add 42    add 43                      
              |         |                    
              v         v                      
        |  |      |  |      |43|      |  |      |  |
        |  |      |42|      |42|      |43|      |  |
                                  |         |  
                                  v         v
                               peek 42    peek 43

    >>> queue = MyQueue()
    >>> queue.size
    0
    >>> queue.add(42)
    >>> queue.size
    1
    >>> queue.add(43)
    >>> queue.size
    2
    >>> queue.peek()
    42
    >>> queue.size
    1
    >>> queue.peek()
    43
    >>> queue.size
    0

    .. warning::

        :class:`MyQueue` is not thread-safe.

    """

    def __init__(self):
        self._size = 0
        self._incoming = MyStack()
        self._outgoing = MyStack()

    @property
    def size(self):
        return self._size

    def add(self, item):
        """Add an item at the top of the queue"""
        self._incoming.add(item)
        self._size += 1

    def peek(self):
        """
        Peek an item from the bottom of the queue
        
        If the stack is empty, raises :class:`myqueue.Empty`.
        """
        if not self._outgoing.size:
            if self._incoming.size:
                self._decant_incoming_into_outgoing()
            else:
                raise Empty("Can't peek item from empty queue")
        item = self._outgoing.peek()
        self._size -= 1
        return item

    def _decant_incoming_into_outgoing(self):
        """Decant all items from incoming into outgoing"""
        while self._incoming.size:
            item = self._incoming.peek()
            self._outgoing.add(item)
