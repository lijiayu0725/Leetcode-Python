class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x // 2 + 1
        while start + 1 < end:
            mid = (start + end) // 2
            if mid ** 2 < x:
                start = mid
            elif mid ** 2 > x:
                end = mid
            else:
                return mid
        if start ** 2 > x:
            return start - 1
        elif start ** 2 == x:
            return start
        if end ** 2 > x:
            return end - 1
        elif end ** 2 == x:
            return end
        return -1


if __name__ == '__main__':
    solution = Solution()
    result = solution.mySqrt(101)
    print(result)
