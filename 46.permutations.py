from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        res = []
        self.dfs(nums, 0, [False] * len(nums), [], res)
        return res

    def dfs(self, nums: List[int], depth: int, used: List[bool], cur: List[int], res: List[List[int]]):
        if depth == len(nums):
            res.append(cur.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            cur.append(nums[i])
            self.dfs(nums, depth + 1, used, cur, res)
            cur.pop()
            used[i] = False


if __name__ == '__main__':
    solution = Solution()
    res = solution.permute([1, 2, 3])
    print(res)
