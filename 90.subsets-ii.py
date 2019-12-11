from typing import *


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums: List[int], start: int, cur: List[int], res: List[List[int]]):
        res.append(cur.copy())
        for i in range(start, len(nums)):
            if i > start and nums[i - 1] == nums[i]:
                continue
            cur.append(nums[i])
            self.dfs(nums, i + 1, cur, res)
            cur.pop()


if __name__ == '__main__':
    solution = Solution()
    result = solution.subsetsWithDup([1, 2, 2])
    print(result)
