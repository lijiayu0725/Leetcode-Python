from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        elif len(prices) == 1:
            return 0
        elif len(prices) == 2:
            return max(0, prices[1] - prices[0])
        dp = [[[0] * 2 for _ in range(3)] for _ in range(len(prices))]
        for i in range(len(prices)):
            for j in range(1, 3):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[-1][-1][0]


if __name__ == '__main__':
    solution = Solution()
    res = solution.maxProfit([1, 2, 3, 4, 5])
    print(res)
