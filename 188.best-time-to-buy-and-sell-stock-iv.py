from typing import *


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        if k > len(prices) / 2:
            return self.maxProfit_inf(prices)
        if len(prices) == 0:
            return 0
        elif len(prices) == 1:
            return 0
        elif len(prices) == 2:
            return max(0, prices[1] - prices[0])
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(len(prices))]
        for i in range(len(prices)):
            for j in range(1, k + 1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[-1][-1][0]

    def maxProfit_inf(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        elif len(prices) == 1:
            return 0
        elif len(prices) == 2:
            return max(0, prices[1] - prices[0])
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]


if __name__ == '__main__':
    solution = Solution()
    res = solution.maxProfit(2, [3, 2, 6, 5, 0, 3])
    print(res)
