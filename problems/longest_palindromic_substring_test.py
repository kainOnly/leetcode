import unittest
from .longest_palindromic_substring import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.longestPalindrome('babad'), 'bab')

    def test_example2(self):
        self.assertEqual(self.sol.longestPalindrome('cbbd'), 'bb')

    def test_example3(self):
        self.assertEqual(self.sol.longestPalindrome('a'), 'a')

    def test_example4(self):
        self.assertEqual(self.sol.longestPalindrome('ac'), 'a')

    def test_example5(self):
        self.assertEqual(self.sol.longestPalindrome('aacabdkacaa'), 'aca')


if __name__ == '__main__':
    unittest.main()
