from typing import *


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = {}
        tmp = 'x' + s[:9]
        for i in range(9, len(s)):
            tmp = tmp[1:] + s[i]
            dic[tmp] = 1 if tmp not in dic else dic[tmp] + 1
        return [k for k, v in dic.items() if v != 1]
