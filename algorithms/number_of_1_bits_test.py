import unittest
from .number_of_1_bits import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.hammingWeight(0b00000000000000000000000000001011), 3)
