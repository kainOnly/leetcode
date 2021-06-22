import unittest
from .palindrome_number import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.isPalindrome(121), True)

    def test_example2(self):
        self.assertEqual(self.sol.isPalindrome(-121), False)

    def test_example3(self):
        self.assertEqual(self.sol.isPalindrome(10), False)

    def test_example4(self):
        self.assertEqual(self.sol.isPalindrome(-101), False)
