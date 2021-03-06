import unittest
from .median_of_two_sorted_arrays import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.findMedianSortedArrays([1, 3], [2]), 2.00000)

    def test_example2(self):
        self.assertEqual(self.sol.findMedianSortedArrays([1, 2], [3, 4]), 2.50000)

    def test_example3(self):
        self.assertEqual(self.sol.findMedianSortedArrays([0, 0], [0, 0]), 0.00000)

    def test_example4(self):
        self.assertEqual(self.sol.findMedianSortedArrays([], [1]), 1.00000)

    def test_example5(self):
        self.assertEqual(self.sol.findMedianSortedArrays([2], []), 2.00000)

    def test_example6(self):
        self.assertEqual(self.sol.findMedianSortedArrays([1, 3, 4, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]), 4.00000)

    def test_example7(self):
        self.assertEqual(self.sol.findMedianSortedArrays([1, 2], [-1, 3]), 1.5)

    def test_example8(self):
        self.assertEqual(self.sol.findMedianSortedArrays([1], [1]), 1)

    def test_example9(self):
        self.assertEqual(self.sol.findMedianSortedArrays([1, 2], [1, 1]), 1)

    def test_example10(self):
        self.assertEqual(self.sol.findMedianSortedArrays([2, 2, 2], [2, 2, 2, 2]), 2)

    def test_example11(self):
        self.assertEqual(self.sol.findMedianSortedArrays([2, 2, 2, 2], [2, 2, 2]), 2)

    def test_example12(self):
        self.assertEqual(self.sol.findMedianSortedArrays([1], [2, 3]), 2)

    def test_example13(self):
        self.assertEqual(self.sol.findMedianSortedArrays([1, 2, 3], [4]), 2.5)

    def test_example14(self):
        self.assertEqual(self.sol.findMedianSortedArrays([5], [1, 2, 3, 4, 6]), 3.5)

    def test_example15(self):
        self.assertEqual(self.sol.findMedianSortedArrays([3, 4], [1, 2, 5, 6]), 3.5)

    def test_example16(self):
        self.assertEqual(self.sol.findMedianSortedArrays([0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 1]), 0.0)

    def test_example17(self):
        self.assertEqual(self.sol.findMedianSortedArrays([1, 3], [2, 7]), 2.5)


if __name__ == '__main__':
    unittest.main()
