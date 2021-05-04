import unittest
from .add_two_numbers import Solution, ListNode


class TestTwoSum(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        l3 = self.sol.addTwoNumbers(l1, l2)
        self.assertEqual(l3.valueOf(), [7, 0, 8])

    def test_example2(self):
        l1 = ListNode(0)
        l2 = ListNode(0)
        l3 = self.sol.addTwoNumbers(l1, l2)
        self.assertEqual(l3.valueOf(), [0])

    def test_example3(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        l3 = self.sol.addTwoNumbers(l1, l2)
        self.assertEqual(l3.valueOf(), [8, 9, 9, 9, 0, 0, 0, 1])


if __name__ == '__main__':
    unittest.main()
