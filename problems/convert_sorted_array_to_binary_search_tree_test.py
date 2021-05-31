import unittest
from collections import deque
from .convert_sorted_array_to_binary_search_tree import Solution, TreeNode


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def get_list(self, root: TreeNode):
        stack, val = deque([root]), []
        while len(stack) != 0:
            node = stack.popleft()
            val.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return val

    def test_example1(self):
        nums = [-10, -3, 0, 5, 9]
        tree = self.sol.sortedArrayToBST(nums)
        self.assertEqual(self.get_list(tree), [0, -10, 5, -3, 9])
