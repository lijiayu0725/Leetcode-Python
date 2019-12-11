from typing import *


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = len(nums) - 1
        while slow <= fast:
            if nums[slow] == val:
                nums[slow] = nums[fast]
                fast -= 1
            else:
                slow += 1
        return fast + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [1]
    res = solution.removeElement(nums, 1)
    print(nums[:res])
