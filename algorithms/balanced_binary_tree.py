# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node: TreeNode):
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1

        if not root:
            return True

        return abs(height(root.left) - height(root.right)) < 2 and \
               self.isBalanced(root.left) and \
               self.isBalanced(root.right)
