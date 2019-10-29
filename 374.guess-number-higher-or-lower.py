from typing import *

def guess(num):
    k = 6
    if num < k:
        return 1
    elif num > k:
        return -1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 0, n
        while start + 1 < end:
            mid = (start + end) // 2
            if guess(mid) == -1:
                end = mid
            elif guess(mid) == 1:
                start = mid
            else:
                return mid
        if guess(start) == 0:
            return start
        if guess(end) == 0:
            return end
        return -1


if __name__ == '__main__':
    solution = Solution()
    result = solution.guessNumber(10)
    print(result)