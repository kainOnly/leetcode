import unittest
from .implement_strstr import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.strStr('hello', 'll'), 2)

    def test_example2(self):
        self.assertEqual(self.sol.strStr('aaaaa', 'bba'), -1)

    def test_example3(self):
        self.assertEqual(self.sol.strStr('', ''), 0)

    def test_example4(self):
        self.assertEqual(self.sol.strStr('mississippi', 'issip'), 4)

    def test_example5(self):
        self.assertEqual(self.sol.strStr('a', 'a'), 0)

    def test_example6(self):
        self.assertEqual(self.sol.strStr('abc', 'c'), 2)
