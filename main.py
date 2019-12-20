from typing import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.partition(nums, 0, len(nums) - 1, len(nums) - k - 1)

    def partition(self, nums, left, right, k):
        if left >= right:
            if right == k - 1:
                return nums[right]
            elif left == k - 1:
                return nums[left]
            else:
                return
        i, j = left, right
        pivot = nums[(left + right) // 2]
        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if (left + right) // 2 > k:
            return self.partition(nums, left, j, k)
        elif (left + right) // 2 < k:
            return self.partition(nums, i, right, k)
        else:
            return pivot


if __name__ == '__main__':
    solution = Solution()
    res = solution.findKthLargest([7, 6, 5, 4, 3, 2, 1], 4)
    print(res)
