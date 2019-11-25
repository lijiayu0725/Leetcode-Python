class Solution:
    def sort(self, nums):
        temp = [0 for _ in range(len(nums))]
        res = [0]
        self.merge_sort(nums, 0, len(nums) - 1, temp, res)
        return res[0]

    def merge_sort(self, nums, start, end, temp, res):
        if start >= end:
            return

        mid = (start + end) // 2

        self.merge_sort(nums, start, mid, temp, res)
        self.merge_sort(nums, mid + 1, end, temp, res)
        self.merge(nums, start, mid, end, temp, res)

    def merge(self, nums, start, mid, end, temp, res):
        left, right = start, mid + 1
        index = start

        while left <= mid and right <= end:
            if nums[left] > nums[right]:
                temp[index] = nums[right]
                res[0] += mid - left + 1
                index += 1
                right += 1
            else:
                temp[index] = nums[left]
                index += 1
                left += 1

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
    res = solution.sort([1,2,3,4,5,6,7,0])
    print(res)
