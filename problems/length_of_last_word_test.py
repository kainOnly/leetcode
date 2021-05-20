import unittest
from .length_of_last_word import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.lengthOfLastWord("Hello World"), 5)

    def test_example2(self):
        self.assertEqual(self.sol.lengthOfLastWord(" "), 0)

    def test_example3(self):
        self.assertEqual(self.sol.lengthOfLastWord("        "), 0)

    def test_example4(self):
        self.assertEqual(self.sol.lengthOfLastWord("a"), 1)

    def test_example5(self):
        self.assertEqual(self.sol.lengthOfLastWord("day"), 3)
