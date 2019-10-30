from typing import *

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * len(triangle) for _ in range(len(triangle))]
        for i in range(len(triangle)):
            dp[len(triangle) - 1][i] = triangle[len(triangle) - 1][i]
        for i in reversed(range(1, len(triangle))):
            for j in range (len(triangle[i]) - 1):
                dp[i - 1][j] = min(dp[i][j], dp[i][j + 1]) + triangle[i - 1][j]
        print(dp)
        return dp[0][0]

if __name__ == '__main__':
    solution = Solution()
    nums = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
    result = solution.minimumTotal(nums)
    print(result)