#!/usr/bin/env python

"""
Implement a. stack data structure.

The :mod:`myqueue.mystack` module provide one class:

* :class:`MyStack`: stack data structure.
"""

from .error import Empty

class MyStack:
    """
    A stack data structure, where items are added and peeked at the top

    For example:
        - Create empty stack.
        - Add items 42 and 43. 
        - Peek these items.

    ::

        |  |    |  |    |43|    |  |    |  |
        |  | -> |42| -> |42| -> |42| -> |  |
        +--+    +--+    +--+    +--+    +--+

    >>> stack = MyStack()
    >>> stack.size
    0
    >>> stack.add(42)
    >>> stack.size
    1
    >>> stack.add(43)
    >>> stack.size
    2
    >>> stack.peek()
    43
    >>> stack.size
    1
    >>> stack.peek()
    42
    >>> stack.size
    0

    .. warning::

        :class:`MyStack` is not thread-safe.
    """

    def __init__(self):
        self._size = 0
        self._items = []

    @property
    def size(self):
        """Number of items in the stack."""
        return self._size

    def add(self, item):
        """Add a item of the top of the stack"""
        self._size += 1
        self._items.append(item)

    def peek(self):
        """
        Peek a item from the top of the stack
        
        If the stack is empty, raises :class:`myqueue.Empty`.
        """
        if self._items:
            item = self._items.pop()
            self._size -= 1
            return item
        else:
            raise Empty("Can't peek item from empty stack")
