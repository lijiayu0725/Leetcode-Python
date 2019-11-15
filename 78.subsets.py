from typing import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if nums == []:
            return res
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, start, cur, res):
        res.append(cur.copy())
        for i in range(start, len(nums)):
            cur.append(nums[i])
            self.dfs(nums, i + 1, cur, res)
            cur.pop()


if __name__ == '__main__':
    solution = Solution()
    result = solution.subsetsWithDup([1,2])
    print(result)