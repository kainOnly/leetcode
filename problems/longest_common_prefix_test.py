import unittest
from .longest_common_prefix import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.longestCommonPrefix(["flower", "flow", "flight"]), 'fl')

    def test_example2(self):
        self.assertEqual(self.sol.longestCommonPrefix(["dog", "racecar", "car"]), '')
