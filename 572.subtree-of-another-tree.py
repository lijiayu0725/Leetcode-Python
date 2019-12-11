# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        return self.isSubtree(s.left, t) or self.isSametree(s, t) or self.isSubtree(s.right, t)

    def isSametree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        else:
            return self.isSametree(s.left, t.left) and s.val == t.val and self.isSametree(s.right, t.right)
