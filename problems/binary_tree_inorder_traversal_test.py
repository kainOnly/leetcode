import unittest
from .binary_tree_inorder_traversal import Solution, TreeNode


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.sol.inorderTraversal(tree), [1, 3, 2])
