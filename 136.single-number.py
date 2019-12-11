from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            res = nums[0]
            for i in range(1, len(nums)):
                res = res ^ nums[i]
            return res
