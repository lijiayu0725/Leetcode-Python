from typing import *


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        res = 0
        res += sum(matrix[0][:])
        res += sum(matrix[:][0])
        res -= matrix[0][0]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    res += dp[i][j]
        return res
