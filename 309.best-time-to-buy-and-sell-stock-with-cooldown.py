from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        elif len(prices) == 1:
            return 0
        elif len(prices) == 2:
            return max(prices[1] - prices[0], 0)
        else:
            dp = [[0] * 2 for _ in range(len(prices))]
            dp[0][1] = -prices[0]
            dp[1][0] = max(0, prices[1] - prices[0])
            dp[1][1] = max(-prices[0], -prices[1])
            for i in range(2, len(prices)):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            return dp[-1][0]


if __name__ == '__main__':
    solution = Solution()
    res = solution.maxProfit([1,2,3,0,2])
    print(res)