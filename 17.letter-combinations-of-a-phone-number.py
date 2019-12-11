from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits is None or len(digits) == 0:
            return []
        res = ['']
        dic = [
            '',
            '',
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz'
        ]
        self.bfs(digits, dic, res)
        res = [item for item in res if len(item) == len(digits)]
        return res

    def dfs(self, nums: str, dic: List[str], i: int, cur: str, res: List[str]):
        if i == len(nums):
            res.append(cur)
            return
        for j in range(len(dic[int(nums[i])])):
            cur += dic[int(nums[i])][j]
            self.dfs(nums, dic, i + 1, cur, res)
            cur = cur[:-1]

    def bfs(self, nums: str, dic: List[str], res: List[str]):
        for n in nums:
            tmp = []
            n = int(n)
            for i, s in enumerate(res):
                for d in dic[n]:
                    tmp.append(s + d)
            res += tmp


if __name__ == '__main__':
    solution = Solution()
    res = solution.letterCombinations('89')
    print(res)
