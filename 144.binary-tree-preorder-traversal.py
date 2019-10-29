from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder

    def preorderTraversal_divide(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result
        left = self.preorderTraversal_divide(root.left)
        right = self.preorderTraversal_divide(root.right)

        result.append(root.val)
        result += left
        result += right

        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution
    print(result)