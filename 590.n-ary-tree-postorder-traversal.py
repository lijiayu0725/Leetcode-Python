from typing import *


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((GRAY, node))
                for child in reversed(node.children):
                    stack.append((WHITE, child))
            else:
                res.append(node.val)
        return res



