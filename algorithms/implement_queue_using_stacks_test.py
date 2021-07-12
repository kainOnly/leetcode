import unittest
from .implement_queue_using_stacks import MyQueue


class Test(unittest.TestCase):

    def test_example1(self):
        my = MyQueue()
        my.push(1)
        my.push(2)
        self.assertEqual(my.peek(), 1)
        self.assertEqual(my.pop(), 1)
        self.assertEqual(my.empty(), False)
