import unittest
from .minimum_depth_of_binary_tree import Solution, TreeNode


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(self.sol.minDepth(tree), 2)

    def test_example2(self):
        tree = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
        self.assertEqual(self.sol.minDepth(tree), 5)
