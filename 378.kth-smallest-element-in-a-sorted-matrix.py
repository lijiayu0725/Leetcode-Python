from typing import *

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        left = matrix[0][0]
        right = matrix[row - 1][col - 1]
        while left + 1 < right:
            mid = (left + right) // 2
            count = self.findSmallerThan(matrix, mid, row, col)
            if count < k:
                left = mid
            elif count > k:
                right = mid
            else:
                right = mid
        if self.findSmallerThan(matrix, left, row, col) >= k:
            return left
        else:
            return right

    def findSmallerThan(self, matrix: List[List[int]], mid: int, row: int, col: int):
        i = 0
        j = col - 1
        count = 0
        while i < row and j >= 0:
            if matrix[i][j] <= mid:
                count += j
                i += 1
            else:
                j -= 1
        return count


if __name__ == '__main__':
    solution = Solution()
    matrix = [
       [ 1,  2],
       [1, 3]
    ]
    res = solution.kthSmallest(matrix, 1)
    print(res)
