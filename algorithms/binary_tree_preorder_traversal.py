# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        val = []
        if not root:
            return val
        node, stack = root, []
        while node or stack:
            while node:
                val.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return val
