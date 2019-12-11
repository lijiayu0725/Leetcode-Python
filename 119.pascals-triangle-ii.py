from typing import *


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for n in range(1, rowIndex + 1):
            for i in reversed(range(1, n)):
                row[i] = row[i - 1] + row[i]
            row.append(1)
        return row


if __name__ == '__main__':
    solution = Solution()
    res = solution.getRow(5)
    print(res)
