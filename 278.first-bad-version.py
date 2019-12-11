def isBadVersion(n):
    return n > 6


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        start, end = 1, n
        while start + 1 < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        if isBadVersion(start):
            return start
        if isBadVersion(end):
            return end
        return -1


if __name__ == '__main__':
    solution = Solution()
    result = solution.firstBadVersion(6)
    print(result)
