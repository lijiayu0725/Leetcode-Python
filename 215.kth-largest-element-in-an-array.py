from typing import *
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    solution = Solution()
    res = solution.findKthLargest([1, 2, 3, 4, 5, 6], 2)
    print(res)
