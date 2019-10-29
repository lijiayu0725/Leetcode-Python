from typing import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                end = mid
            elif nums[mid] > target:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])



if __name__ == '__main__':
    solution = Solution()
    result = solution.findMin([1,2,3,4,5,6,7])
    print(result)