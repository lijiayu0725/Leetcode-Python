from typing import *

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if len(S) == 0:
            return []
        res = []
        self.dfs(S, 0, '', res)
        return res

    def dfs(self, S: str, start: int, cur: str, res: List[str]):
        if start == len(S):
            res.append(cur)
            return
        if S[start].isdigit():
            self.dfs(S, start + 1, cur + S[start], res)
        else:
            self.dfs(S, start + 1, cur + S[start].upper(), res)
            self.dfs(S, start + 1, cur + S[start].lower(), res)


if __name__ == '__main__':
    solution = Solution()
    res = solution.letterCasePermutation('a1b2')
    print(res)
