.. myqueue documentation master file, created by
   sphinx-quickstart on Sat Sep 19 11:18:54 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to myqueue's documentation!
###################################

`myqueue` implements a queue with 2 stacks, for demo purpose.

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

myqueue package API
####################################

.. toctree::
   :maxdepth: 4

   mystack
   myqueue

Developer guide
####################################

.. toctree::
   :maxdepth: 4

   develop
   doc


Indices and tables
##################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

