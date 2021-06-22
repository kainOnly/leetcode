import unittest
from .remove_duplicates_from_sorted_list import Solution, ListNode


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        n = ListNode(1, ListNode(1, ListNode(2)))
        result = self.sol.deleteDuplicates(n)
        self.assertEqual(result.values(), [1, 2])

    def test_example2(self):
        n = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        result = self.sol.deleteDuplicates(n)
        self.assertEqual(result.values(), [1, 2, 3])
