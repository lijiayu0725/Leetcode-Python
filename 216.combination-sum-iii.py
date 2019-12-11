from typing import *


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k == 0 or n == 0:
            return []
        res = []
        self.dfs(k, n, 1, 0, [], res)
        return res

    def dfs(self, nums: int, target: int, start: int, sum: int, cur: List[int], res: List[List[int]]):
        if sum > target:
            return
        elif sum == target and len(cur) == nums:
            res.append(cur.copy())
        else:
            for i in range(start, 10):
                cur.append(i)
                self.dfs(nums, target, i + 1, sum + i, cur, res)
                cur.pop()


if __name__ == '__main__':
    solution = Solution()
    res = solution.combinationSum3(3, 9)
    print(res)
