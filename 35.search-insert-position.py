from typing import *

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None:
            return -1
        if len(nums) == 0:
            return 0
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[end] < target:
            return end + 1
        if nums[start] < target:
            return end
        return 0

if __name__ == '__main__':
    solution = Solution()
    result = solution.searchInsert([-1,0,2,3,4], 0)
    print(result)