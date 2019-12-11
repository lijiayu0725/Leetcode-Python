from typing import *


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left + 1 < right:
            mid = (left + right) // 2
            count = self.findSmallerThan(matrix, mid)
            if count < k:
                left = mid
            elif count > k:
                right = mid
            else:
                right = mid
        if self.findSmallerThan(matrix, left) >= k:
            return left
        else:
            return right

    def findSmallerThan(self, matrix: List[List[int]], mid: int):
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = col - 1
        count = 0
        while i < row and j >= 0:
            if matrix[i][j] <= mid:
                count += j + 1
                i += 1
            else:
                j -= 1
        return count


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    res = solution.kthSmallest(matrix, 8)
    print(res)
