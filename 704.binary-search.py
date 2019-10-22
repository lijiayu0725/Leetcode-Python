from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


if __name__ == '__main__':
    solution = Solution()
    result = solution.search([1,2,3,4,5], 12)
    print(result)