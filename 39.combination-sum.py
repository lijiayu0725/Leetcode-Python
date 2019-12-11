from typing import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, 0, 0, [], res)
        return res

    def dfs(self, candidates: List[int], target: int, sum: int, i: int, cur: List[int], res: List[List[int]]):
        if sum > target:
            return
        elif sum == target:
            res.append(cur.copy())
        else:
            for num in candidates[i:]:
                cur.append(num)
                self.dfs(candidates, target, sum + num, candidates.index(num), cur, res)
                cur.pop()


if __name__ == '__main__':
    solution = Solution()
    res = solution.combinationSum([2, 3, 4], 8)
    print(res)
