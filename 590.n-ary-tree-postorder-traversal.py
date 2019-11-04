from typing import *


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root is None:
            return res
        for i in range(len(root.children)):
            res += self.postorder(root.children[i])
        res.append(root.val)
        return res



