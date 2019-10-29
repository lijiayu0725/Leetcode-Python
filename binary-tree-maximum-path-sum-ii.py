from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.maxPathSum2(root.left)
        right = self.maxPathSum2(root.right)
        return max(0, max(left, right)) + root.val
