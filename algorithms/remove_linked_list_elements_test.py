import unittest
from .remove_linked_list_elements import Solution, ListNode


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(7)))))))
        self.assertEqual(self.sol.removeElements(head, 6).valueOf(), [1, 2, 3, 4, 5, 7])
