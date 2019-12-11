from typing import *


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [str(i) for i in range(1, n + 1)]
        res.sort()
        return [int(i) for i in res]


if __name__ == '__main__':
    solution = Solution()
    res = solution.lexicalOrder(13)
    print(res)
