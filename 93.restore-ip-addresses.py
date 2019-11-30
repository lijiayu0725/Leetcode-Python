from typing import *

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        res = []
        self.dfs(0, s, [], res)
        return res

    def dfs(self, start: int, s: str, segment: List[str], res: List[str]):
        if len(segment) == 4:
            if len(s) == start:
                res.append('.'.join(segment))
            return
        for i in range(1, 4):
            if start + i > len(s):
                break
            tmp = s[start: start + i]
            if (tmp[0] == '0' and len(tmp) > 1) or i == 3 and int(tmp) > 255:
                break
            segment.append(tmp)
            self.dfs(start + i, s, segment, res)
            segment.pop()


if __name__ == '__main__':
    solution = Solution()
    res = solution.restoreIpAddresses("19216827")
    print(res)