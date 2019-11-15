from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            if sum == 0:
                return True
            else:
                return False
        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)
        return left or right
