class Solution:
    def convertToTitle(self, n: int) -> str:
        res = []
        while n > 0:
            n -= 1
            tmp = n % 26
            alpha = chr(ord('A') + tmp)
            res.insert(0, alpha)
            n //= 26
        return ''.join(res)
