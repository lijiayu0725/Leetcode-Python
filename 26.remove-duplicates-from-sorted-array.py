from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
            fast += 1
        return slow + 1
