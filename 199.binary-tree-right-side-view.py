from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
        return res
