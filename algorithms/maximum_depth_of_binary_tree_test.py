import unittest
from .maximum_depth_of_binary_tree import Solution, TreeNode


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        tree = TreeNode(
            3,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7))
        )
        self.assertEqual(self.sol.maxDepth(tree), 3)
