import unittest
from .linked_list_cycle import Solution, ListNode


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        l0 = ListNode(3)
        l1 = ListNode(2)
        l2 = ListNode(0)
        l3 = ListNode(-4)
        l0.next = l1
        l1.next = l2
        l2.next = l3
        l3.next = l1
        self.assertEqual(self.sol.hasCycle(l0), True)
