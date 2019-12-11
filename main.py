import math

class Solution:
    def log(self, b, x, eps=0.000000000000001):
        left = 1
        right = x
        while left + eps < right:
            mid = (left + right) / 2
            if b ** mid > x:
                right = mid
            else:
                left = mid
        return left

if __name__ == '__main__':
    solution = Solution()
    res = solution.log(2, 1000)
    print(res, math.log(1000, 2))
    a = []
    a.clear()