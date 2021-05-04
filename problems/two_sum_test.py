import unittest
from .two_sum import Solution


class TestTwoSum(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_example2(self):
        self.assertEqual(self.sol.twoSum([3, 2, 4], 6), [1, 2])

    def test_example3(self):
        self.assertEqual(self.sol.twoSum([3, 3], 6), [0, 1])


if __name__ == '__main__':
    unittest.main()
