import unittest
from .valid_parentheses import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.isValid('()'), True)

    def test_example2(self):
        self.assertEqual(self.sol.isValid('()[]{}'), True)

    def test_example3(self):
        self.assertEqual(self.sol.isValid('(]'), False)

    def test_example4(self):
        self.assertEqual(self.sol.isValid('([)]'), False)

    def test_example5(self):
        self.assertEqual(self.sol.isValid('{[]}'), True)

    def test_example6(self):
        self.assertEqual(self.sol.isValid('(('), False)

    def test_example7(self):
        self.assertEqual(self.sol.isValid('(]'), False)
