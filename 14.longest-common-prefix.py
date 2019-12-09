from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        last = 0
        minl = min([len(s) for s in strs])
        while last < minl:
            for i in range(1, len(strs)):
                if strs[i][last] != strs[i - 1][last]:
                    return strs[0][:last]
            last += 1
        return strs[0][:last]

if __name__ == '__main__':
    solution = Solution()
    res = solution.longestCommonPrefix(['flower', 'flow', 'flight'])
    print(res)

