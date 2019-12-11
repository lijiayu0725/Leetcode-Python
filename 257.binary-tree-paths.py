from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.dfs(root, [str(root.val)], res)
        return res

    def dfs(self, root, cur, res):
        if root.left is None and root.right is None:
            res.append('->'.join(cur))
            return
        if root.left:
            cur.append(str(root.left.val))
            self.dfs(root.left, cur, res)
            cur.pop()
        if root.right:
            cur.append(str(root.right.val))
            self.dfs(root.right, cur, res)
            cur.pop()
