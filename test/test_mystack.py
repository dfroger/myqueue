import unittest

import myqueue

class TestMyStack(unittest.TestCase):

    def test_empty_stack(self):
        stack = myqueue.MyStack()
        self.assertEqual(stack.size, 0)

    def test_add_and_peek_one_item(self):
        # Create empty stack
        stack = myqueue.MyStack()

        # Add item 42
        stack.add(42)
        self.assertEqual(stack.size, 1)

        # Peek item 42
        item = stack.peek()
        self.assertEqual(stack.size, 0)
        self.assertEqual(item, 42)

    def test_add_and_peek_two_items(self):
        # Create empty stack
        stack = myqueue.MyStack()

        # Add item 42
        stack.add(42)
        self.assertEqual(stack.size, 1)

        # Add item 43
        stack.add(43)
        self.assertEqual(stack.size, 2)

        # Peek item 43
        item = stack.peek()
        self.assertEqual(stack.size, 1)
        self.assertEqual(item, 43)

        # Peek item 43
        item = stack.peek()
        self.assertEqual(stack.size, 0)
        self.assertEqual(item, 42)

    def test_peek_empty_stack(self):
        # Create empty stack
        stack = myqueue.MyStack()

        msg = "Can't peek item from empty stack"
        with self.assertRaisesRegexp(myqueue.Empty, msg):
            stack.peek()

if __name__ == '__main__':
    unittest.main()
