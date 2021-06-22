import unittest
from .same_tree import Solution, TreeNode


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
        tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(self.sol.isSameTree(tree1, tree2), True)

    def test_example2(self):
        tree1 = TreeNode(1, TreeNode(2))
        tree2 = TreeNode(1, None, TreeNode(2))
        self.assertEqual(self.sol.isSameTree(tree1, tree2), False)

    def test_example3(self):
        tree1 = TreeNode(1, TreeNode(2), TreeNode(1))
        tree2 = TreeNode(1, TreeNode(1), TreeNode(2))
        self.assertEqual(self.sol.isSameTree(tree1, tree2), False)
