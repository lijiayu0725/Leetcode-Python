from typing import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1
        min = nums[0]
        for num in nums:
            if num < min:
                min = num
        return min

if __name__ == '__main__':
    solution = Solution()
    result = solution.findMin([2,2,2,0,1])
    print(result)