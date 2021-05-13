import unittest
from .merge_two_sorted_lists import Solution, ListNode


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        l1 = ListNode(1, ListNode(2, ListNode(4)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        l3 = self.sol.mergeTwoLists(l1, l2)
        self.assertEqual(l3.valueOf(), [1, 1, 2, 3, 4, 4])

