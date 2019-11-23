from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        for i, num in enumerate(nums):
            tmp = dic.get(target - num)
            if tmp is not None and tmp != i:
                return [i, tmp]