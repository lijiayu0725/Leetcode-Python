from typing import *

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if A is None or len(A) < 3:
            return -1
        start, end = 1, len(A) - 2
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid - 1] < A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid
        if A[start - 1] < A[start] and A[start] > A[start + 1]:
            return start
        if A[end - 1] < A[end] and A[end] > A[end + 1]:
            return end
        return -1


if __name__ == '__main__':
    solution = Solution()
    result = solution.peakIndexInMountainArray([0,1,2,0])
    print(result)