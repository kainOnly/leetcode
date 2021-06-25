import unittest
from .reverse_bits import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.reverseBits(0b0000010100101000001111010011100), 0b0111001011110000010100101000000)
