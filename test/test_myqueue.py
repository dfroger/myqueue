import unittest

import myqueue

class TestMyQueue(unittest.TestCase):

    def test_empty_queue(self):
        queue = myqueue.MyQueue()
        self.assertEqual(queue.size, 0)

    def test_add_and_peek_one_item(self):
        # Create an empty queue.
        queue = myqueue.MyQueue()
        self.assertEqual(queue.size, 0)

        # Add item 42
        queue.add(42)
        self.assertEqual(queue.size, 1)

        # Peek item item 42
        item = queue.peek()
        self.assertEqual(queue.size, 0)
        self.assertEqual(item, 42)

    def test_add_and_peek_two_items(self):
        # Create an empty queue.
        queue = myqueue.MyQueue()
        self.assertEqual(queue.size, 0)

        # Add item 42
        queue.add(42)
        self.assertEqual(queue.size, 1)

        # Add item 43
        queue.add(43)
        self.assertEqual(queue.size, 2)

        # Peek item item 42
        item = queue.peek()
        self.assertEqual(queue.size, 1)
        self.assertEqual(item, 42)

        # Peek item item 43
        item = queue.peek()
        self.assertEqual(queue.size, 0)
        self.assertEqual(item, 43)

    def test_peek_empty_queue(self):
        # Create empty queue
        queue = myqueue.MyQueue()

        msg = "Can't peek item from empty queue"
        with self.assertRaisesRegexp(myqueue.Empty, msg):
            queue.peek()

if __name__ == '__main__':
    unittest.main()
