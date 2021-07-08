import unittest
from .implement_stack_using_queues import MyStack


class Test(unittest.TestCase):
    def test_example(self):
        mystack = MyStack()
        mystack.push(1)
        mystack.push(2)
        self.assertEqual(mystack.top(), 2)
        self.assertEqual(mystack.pop(), 2)
        self.assertEqual(mystack.empty(), False)
