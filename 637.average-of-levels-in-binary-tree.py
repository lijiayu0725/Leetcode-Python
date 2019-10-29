from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            size = len(queue)
            sum = 0
            for i in range(size):
                node = queue.pop()
                sum += node.val
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
            result.append(sum / size)
        return result