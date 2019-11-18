from typing import *

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            m = max(nums)
            count = [0 for _ in range(m + 1)]
            for n in nums:
                count[n] += 1
            dp = [0 for _ in range(len(count))]
            dp[0] = 0
            dp[1] = 1 * count[1]

            for i in range(2, m + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + i * count[i])
            return dp[-1]



if __name__ == '__main__':
    solution = Solution()
    res = solution.deleteAndEarn([2, 2, 3, 3, 3, 4])
    print(res)