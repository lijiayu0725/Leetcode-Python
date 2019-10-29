from typing import *

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    solution = Solution()
    result = solution.intersection([0,1,2,0], [1])
    print(result)