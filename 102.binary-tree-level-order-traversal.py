from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = []
        queue.append(root)
        while queue:
            lenth = len(queue)
            res = []
            for i in range(lenth):
                node = queue.pop()
                res.append(node.val)
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
            result.append(res)
        return result
