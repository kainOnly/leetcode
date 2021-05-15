import unittest
from .remove_element import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.removeElement([3, 2, 2, 3], 3), 2)

    def test_example2(self):
        self.assertEqual(self.sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)
