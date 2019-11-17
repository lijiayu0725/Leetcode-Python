from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] : 到第i个数的最大子序列和
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i]
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    res = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(res)