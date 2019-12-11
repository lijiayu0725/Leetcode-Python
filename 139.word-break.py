from typing import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.helper(s, wordDict, {})

    def helper(self, s: str, wordDict: List[str], mem) -> bool:
        if s in mem:
            return mem[s]
        if s in wordDict:
            mem[s] = True
            return True
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            if left in wordDict and self.helper(right, wordDict, mem):
                mem[s] = True
                return True
        mem[s] = False
        return False


if __name__ == '__main__':
    solution = Solution()
    res = solution.wordBreak("leet", ["lee", "code"])
    print(res)
