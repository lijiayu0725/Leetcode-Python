class Solution:
    def titleToNumber(self, s: str) -> int:
        exp = 1
        s = list(s)
        s.reverse()
        res = 0
        for c in s:
            res += exp * (ord(c) - ord('A') + 1)
        return res
