import unittest

import myqueue

class TestMyQueue(unittest.TestCase):

    def test_empty_queue(self):
        queue = myqueue.MyQueue()
        self.assertEqual(queue.size, 0)

    def test_add(self):
        # Create an empty queue.
        queue = myqueue.MyQueue()
        self.assertEqual(queue.size, 0)

        # Add a item in the queue.
        queue.add(42)
        self.assertEqual(queue.size, 1)

        # Peek a item from the queue.
        item = queue.peek()
        self.assertEqual(queue.size, 0)
        #self.assertEqual(item, 42)
