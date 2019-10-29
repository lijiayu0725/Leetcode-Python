from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root)[0]

    def helper(self, root: TreeNode) -> Tuple[bool, int]:
        if root is None:
            return True, 0
        left_balanced, left_depth = self.helper(root.left)
        right_balanced, right_depth = self.helper(root.right)
        if left_balanced and right_balanced and abs(left_depth - right_depth) <= 1:
            return True, max(left_depth, right_depth) + 1
        else:
            return False, 0


if __name__ == '__main__':
    solution = Solution()
    result = solution.isBalanced()
    print(result)