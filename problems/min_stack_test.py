import unittest
from .min_stack import MinStack


class Test(unittest.TestCase):
    def test_example1(self):
        n = MinStack()
        n.push(-2)
        n.push(0)
        n.push(-3)
        self.assertEqual(n.getMin(), -3)
        n.pop()
        self.assertEqual(n.top(), 0)
        self.assertEqual(n.getMin(), -2)
