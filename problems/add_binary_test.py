import unittest
from .add_binary import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.addBinary('11', '1'), '100')

    def test_example2(self):
        self.assertEqual(self.sol.addBinary('1010', '1011'), '10101')
