class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
