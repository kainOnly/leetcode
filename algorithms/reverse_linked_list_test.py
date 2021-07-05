import unittest
from .reverse_linked_list import Solution, ListNode


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual(self.sol.reverseList(head).toList(), [5, 4, 3, 2, 1])
