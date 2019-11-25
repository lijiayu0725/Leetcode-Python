from typing import *

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x_max = len(matrix)
        y_max = len(matrix[0])
        x, y = 0, 0
        res = []
        while x <= x_max // 2 and y <= y_max // 2:
            self.prin(matrix, (x, y), (x_max - x - 1, y_max - y - 1), res)
            x += 1
            y += 1
        return res

    def prin(self, matrix: List[List[int]], left: Tuple[int, int], right: Tuple[int, int], res: List[int]) -> None:
        if left == right:
            res.append(matrix[left[0]][left[1]])
            return
        left_x, left_y = left
        right_x, right_y = right
        x, y = left_x, left_y
        while y < right_y:
            res.append(matrix[x][y])
            y += 1

        while x < right_x:
            res.append(matrix[x][y])
            x += 1

        while y > left_y:
            res.append(matrix[x][y])
            y -= 1

        while x > left_x:
            res.append(matrix[x][y])
            x -= 1


if __name__ == '__main__':
    solution = Solution()
    res = solution.spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    print(res)