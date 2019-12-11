from typing import *


class Solution:
    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        start, end = 0, len(matrix) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        if matrix[end][0] <= target:
            row = end
        else:
            row = start

        start, end = 0, len(matrix[row]) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if (matrix[row][mid] == target):
                return True
            elif (matrix[row][mid] < target):
                start = mid
            else:
                end = mid
        if matrix[row][start] == target or matrix[row][end] == target:
            return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] < target:
                start = mid
            else:
                end = mid
        if matrix[start // n][start % n] == target or matrix[end // n][end % n] == target:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    result = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 1)
    print(result)
