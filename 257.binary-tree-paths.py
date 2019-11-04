from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        res = ''
        self.helper(root, res, result)
        return result

    def helper(self, root: TreeNode, res: str, result: List[str]):
        if root is None:
            return
        res += str(root.val)
        if root.left is None and root.right is None:
            result.append(res)
        else:
            res += '->'
            self.helper(root.left, res, result)
            self.helper(root.right, res, result)

