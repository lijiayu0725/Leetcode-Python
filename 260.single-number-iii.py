from typing import *

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums[0]]
        else:
            s = set()
            for i in range(len(nums)):
                if nums[i] in s:
                    s.remove(nums[i])
                else:
                    s.add(nums[i])
            return list(s)
