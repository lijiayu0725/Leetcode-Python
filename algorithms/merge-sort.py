class Solution:
    def sort(self, nums):
        temp = [0 for _ in range(len(nums))]
        self.merge_sort(nums, 0, len(nums) - 1, temp)

    def merge_sort(self, nums, start, end, temp):
        if start >= end:
            return

        mid = (start + end) // 2

        self.merge_sort(nums, start, mid, temp)
        self.merge_sort(nums, mid + 1, end, temp)
        self.merge(nums, start, mid, end, temp)

    def merge(self, nums, start, mid, end, temp):
        left, right = start, mid + 1
        index = start

        while left <= mid and right <= end:
            if nums[left] < nums[right]:
                temp[index] = nums[left]
                index += 1
                left += 1
            else:
                temp[index] = nums[right]
                index += 1
                right += 1

        while left <= mid:
            temp[index] = nums[left]
            index += 1
            left += 1
        while right <= end:
            temp[index] = nums[right]
            index += 1
            right += 1

        for index in range(start, end + 1):
            nums[index] = temp[index]


if __name__ == '__main__':
    solution = Solution()
    result = [7,6,5,4,3,2,1]
    solution.sort(result)
    print(result)