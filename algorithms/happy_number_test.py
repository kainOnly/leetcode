import unittest
from .happy_number import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.isHappy(19), True)

    def test_example2(self):
        self.assertEqual(self.sol.isHappy(2), False)
