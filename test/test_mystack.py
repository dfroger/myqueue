import unittest

import myqueue

class TestMyStack(unittest.TestCase):

    def test_empty_stack(self):
        stack = myqueue.MyStack()
        self.assertEqual(stack.size, 0)

    def test_add(self):
        # Create empty stack
        stack = myqueue.MyStack()

        # Add item 42
        stack.add(42)
        self.assertEqual(stack.size, 1)

        # Peek item
        item = stack.peek()
        self.assertEqual(stack.size, 0)



if __name__ == '__main__':
    unittest.main()
