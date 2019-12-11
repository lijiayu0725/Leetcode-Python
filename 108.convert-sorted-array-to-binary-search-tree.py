from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums: List[int], start: int, end: int) -> TreeNode:
        if start <= end:
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = self.helper(nums, start, mid - 1)
            root.right = self.helper(nums, mid + 1, end)
            return root
