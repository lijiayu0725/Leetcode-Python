from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return self.helper(root)[1]

    def helper(self, root: TreeNode) -> Tuple[int, int]:
        if root is None:
            return -float('inf'), -float('inf')
        left_root2any, left_any2any = self.helper(root.left)
        right_root2any, right_any2any = self.helper(root.right)

        root2any = root.val + max(0, max(left_root2any, right_root2any))

        any2any = max(left_any2any, right_any2any)

        any2any = max(any2any, max(left_root2any, 0) + root.val + max(right_root2any, 0))

        return root2any, any2any


if __name__ == '__main__':
    pass
