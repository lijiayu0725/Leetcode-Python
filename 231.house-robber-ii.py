from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            dp = [[0] * 2 for _ in range(len(nums))]
            dp[0][0] = 0
            dp[1][0] = nums[1]
            dp[0][1] = nums[0]
            dp[1][1] = nums[0]
            for i in range(2, len(nums)):
                dp[i][0] = max(dp[i - 2][0] + nums[i], dp[i - 1][0])
                dp[i][1] = max(dp[i - 2][1] + nums[i], dp[i - 1][1])
            return max(dp[-1][0], dp[-2][1])



if __name__ == '__main__':
    solution = Solution()
    res = solution.rob([1,2,3,1])
    print(res)