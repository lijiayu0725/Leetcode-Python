from typing import *


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0 or n == 0:
            return []
        res = []
        self.dfs(n, k, 1, [], res)
        return res

    def dfs(self, end: int, nums: int, start: int, cur: List[int], res: List[List[int]]):
        if len(cur) == nums:
            res.append(cur.copy())
            return
        for num in range(start, end + 1):
            cur.append(num)
            self.dfs(end, nums, num + 1, cur, res)
            cur.pop()


if __name__ == '__main__':
    solution = Solution()
    res = solution.combine(4, 2)
    print(res)
