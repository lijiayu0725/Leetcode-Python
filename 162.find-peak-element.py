from typing import *


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return int(nums[0] < nums[1])
        start, end = 1, len(nums) - 2
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                start = mid
            elif nums[start] < nums[end]:
                start = mid
            else:
                end = mid
        if nums[start] > nums[start - 1] and nums[start] > nums[start + 1]:
            return start
        if nums[end] > nums[end - 1] and nums[end] > nums[end + 1]:
            return end
        if nums[0] < nums[-1]:
            return len(nums) - 1
        if nums[0] > nums[-1]:
            return 0
        return 0


if __name__ == '__main__':
    solution = Solution()
    result = solution.findPeakElement([2, 3, 4])
    print(result)
