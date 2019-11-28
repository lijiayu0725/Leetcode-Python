from typing import *

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        dp = [0 for _ in range(len(A))]
        dp[0] = A[0]
        res = []
        for i in range(1, len(A)):
            dp[i] = dp[i - 1] + A[i] if dp[i - 1] > 0 else A[i]
        res.append(max(dp))

        dp = [0 for _ in range(len(A))]
        dp[0] = A[0]
        for i in range(1, len(A)):
            dp[i] = dp[i - 1] + A[i] if dp[i - 1] < 0 else A[i]
        res.append(sum(A) - min(dp))

        return max(res)
