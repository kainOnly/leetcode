import unittest
from .valid_palindrome import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.isPalindrome('A man, a plan, a canal: Panama'), True)

    def test_example2(self):
        self.assertEqual(self.sol.isPalindrome('race a car'), False)
