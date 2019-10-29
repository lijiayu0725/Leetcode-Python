from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            size = len(queue)
            res = []
            for i in range(size):
                node = queue.pop()
                res.append(node.val)
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
            result.insert(0, res)
        return result