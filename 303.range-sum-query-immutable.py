from typing import *


class NumArray:

    def __init__(self, nums: List[int]):
        # self.sum: i 前面数的和
        self.sum = [0 for i in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            self.sum[i] = self.sum[i - 1] + nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j + 1] - self.sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    i = 0
    j = 5
    param_1 = obj.sumRange(i, j)
    print(param_1)
