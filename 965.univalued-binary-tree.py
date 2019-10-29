from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left = self.isUnivalTree(root.left)
        right = self.isUnivalTree(root.right)
        left_bool, right_bool = True, True
        if root.left:
            left_bool = (root.left.val == root.val)
        if root.right:
            right_bool = (root.right.val == root.val)
        return left and right and left_bool and right_bool