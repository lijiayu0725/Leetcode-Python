from typing import *


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res = up = down = 0
        for i in range(1, len(A)):
            if (down and A[i - 1] < A[i]) or A[i - 1] == A[i]:
                up = 0
                down = 0
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down:
                res = max(res, up + down + 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.longestMountain([2, 1, 4, 7, 7, 7, 3, 2, 5])
    print(res)
