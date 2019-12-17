from typing import *

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] % 2 == 0 and A[right] % 2 == 1:
                left += 1
                right -= 1
                continue
            elif A[left] % 2 == 1 and A[right] % 2 == 0:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
            elif A[left] % 2 == 1 and A[right] % 2 == 1:
                right -= 1
            else:
                left += 1
        return A

if __name__ == '__main__':
    solution = Solution()
    res = solution.sortArrayByParity([0,1,2])
    print(res)

