from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.helper(root, root)

    def helper(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        elif p is None and q is None:
            return True
        else:
            first = self.helper(p.left, q.right)
            second = self.helper(p.right, q.left)
            return first and second and p.val == q.val