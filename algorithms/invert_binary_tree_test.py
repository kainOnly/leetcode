import unittest
from .invert_binary_tree import Solution, TreeNode


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
        self.assertEqual(self.sol.invertTree(root).toList(), [9, 6, 7, 3, 1, 2, 4])
