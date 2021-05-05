import unittest
from .longest_substring_without_repeating_characters import Solution


class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('abcabcbb'), 3)

    def test_example2(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('bbbbb'), 1)

    def test_example3(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('pwwkew'), 3)

    def test_example4(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring(' '), 1)

    def test_example5(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('aab'), 2)

    def test_example6(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('cdd'), 2)

    def test_example7(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('dvdf'), 3)


if __name__ == '__main__':
    unittest.main()
