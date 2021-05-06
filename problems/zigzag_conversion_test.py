import unittest
from .zigzag_conversion import Solution


class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')

    def test_example2(self):
        self.assertEqual(self.sol.convert('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')

    def test_example3(self):
        self.assertEqual(self.sol.convert('A', 1), 'A')


if __name__ == '__main__':
    unittest.main()
