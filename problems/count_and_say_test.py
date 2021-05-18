import unittest
from .count_and_say import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.countAndSay(1), '1')

    def test_example2(self):
        self.assertEqual(self.sol.countAndSay(4), '1211')
