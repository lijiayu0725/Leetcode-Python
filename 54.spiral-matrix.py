from typing import *


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        x_max = len(matrix) - 1
        y_max = len(matrix[0]) - 1
        x, y = 0, 0
        res = []
        while x <= x_max and y <= y_max:
            self.matrix_print(matrix, (x, y), (x_max, y_max), res)
            x += 1
            y += 1
            x_max -= 1
            y_max -= 1
        return res

    def matrix_print(self, matrix: List[List[int]], left, right, res: List[int]) -> None:
        i, j = left
        if left[0] == right[0]:
            res += matrix[left[0]][left[1]: right[1] + 1]
            return
        elif left[1] == right[1]:
            for i in range(left[0], right[0] + 1):
                res.append(matrix[i][left[1]])
            return
        while j < right[1]:
            res.append(matrix[i][j])
            j += 1
        while i < right[0]:
            res.append(matrix[i][j])
            i += 1
        while j > left[1]:
            res.append(matrix[i][j])
            j -= 1
        while i > left[0]:
            res.append(matrix[i][j])
            i -= 1


if __name__ == '__main__':
    solution = Solution()
    res = solution.spiralOrder([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]])
    print(res)
