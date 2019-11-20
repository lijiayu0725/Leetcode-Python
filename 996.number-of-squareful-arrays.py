from typing import *
import math


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        A.sort()
        res = []
        self.dfs(A, 0, [False] * len(A), [], res)
        return len(res)


    def dfs(self, A: List[int], depth: int, used: List[bool], cur: List[int], res: List[List[int]]):
        if depth == len(A):
            res.append(cur.copy())
        for i in range(len(A)):
            if used[i]:
                continue
            if i > 0 and A[i] == A[i - 1] and not used[i - 1]:
                continue
            if not cur or math.sqrt(cur[-1] + A[i]) % 1 == 0:
                used[i] = True
                cur.append(A[i])
                self.dfs(A, depth + 1, used, cur, res)
                used[i] = False
                cur.pop()

if __name__ == '__main__':
    solution = Solution()
    res = solution.numSquarefulPerms([2,2,2])
    print(res)