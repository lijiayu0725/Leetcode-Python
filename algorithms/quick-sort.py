class Solution:
    def sort(self, nums):
        self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, nums, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end)

if __name__ == '__main__':
    solution = Solution()
    nums = [7,6,5,4,3,2,1]
    solution.sort(nums)
    print(nums)