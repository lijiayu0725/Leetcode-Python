from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in dic:
                if i == dic[nums[i]]:
                    continue
                return [i, dic[nums[i]]]
