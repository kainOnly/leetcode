# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def toList(self):
        val = []
        root = self
        prev, stack = None, []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                val.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return val


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left

        return root
