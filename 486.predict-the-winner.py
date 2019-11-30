from typing import *

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][-1] >= 0

if __name__ == '__main__':
    solution = Solution()
    res = solution.PredictTheWinner([1, 5, 2])
    print(res)