import unittest
from .symmetric_tree import Solution, TreeNode


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        node1 = TreeNode(2, TreeNode(3), TreeNode(4))
        node2 = TreeNode(2, TreeNode(4), TreeNode(3))
        root = TreeNode(1, node1, node2)
        self.assertEqual(self.sol.isSymmetric(root), True)

    def test_example2(self):
        node1 = TreeNode(2, None, TreeNode(3))
        node2 = TreeNode(2, None, TreeNode(3))
        root = TreeNode(1, node1, node2)
        self.assertEqual(self.sol.isSymmetric(root), False)
