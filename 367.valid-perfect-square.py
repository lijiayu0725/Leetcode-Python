class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 0, num
        while start + 1 < end:
            mid = (start + end) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                end = mid
            else:
                start = mid
        if start ** 2 == num or end ** 2 == num:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    result = solution.isPerfectSquare(0)
    print(result)
