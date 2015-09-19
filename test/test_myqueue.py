import unittest

import myqueue

class TestMyQueue(unittest.TestCase):

    def test_empty_queue(self):
        queue = myqueue.MyQueue()
        self.assertEqual(queue.size, 0)
