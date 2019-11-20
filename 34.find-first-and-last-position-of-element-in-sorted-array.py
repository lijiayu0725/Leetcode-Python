from typing import *

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        res = []
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid
            elif target < nums[mid]:
                right = mid
            else:
                right = mid
        if nums[left] == target:
            res.append(left)
        elif nums[right] == target:
            res.append(right)
        else:
            res.append(-1)

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid
        if nums[right] == target:
            res.append(right)
        elif nums[left] == target:
            res.append(left)
        else:
            res.append(-1)
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.searchRange([1,2,3,3,3,4,5], 3)
    print(res)