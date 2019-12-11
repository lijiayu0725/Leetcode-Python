from typing import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return []
        elif len(candidates) == 0:
            return []
        else:
            res = []
            candidates = sorted(candidates)
            self.dfs(candidates, target, 0, 0, 0, [], res)
            return res

    def dfs(self, nums: List[int], target: int, deep: int, sum: int, j: int, cur: List[int], res: List[List[int]]):
        if sum == target:
            res.append(cur.copy())
        else:
            for i in range(j, len(nums)):
                if i != j and nums[i] == nums[i - 1]:
                    continue
                if nums[i] + sum > target:
                    continue
                cur.append(nums[i])
                self.dfs(nums, target, deep + 1, sum + nums[i], i + 1, cur, res)
                cur.pop()


if __name__ == '__main__':
    solution = Solution()
    res = solution.combinationSum2([1, 2, 3, 4, 5], 7)
    print(res)
