from typing import *

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) == 0:
            return []
        nums = sorted(nums)
        results = []
        self.subsetshelper(nums, results, [], 0)
        return results

    def subsetshelper(self, nums: List[int], results: List[List[int]], subset: List[int], startIndex: int):
        results.append(subset.copy())
        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self.subsetshelper(nums, results, subset, i + 1)
            subset.pop()


if __name__ == '__main__':
    solution = Solution()
    result = solution.subsetsWithDup([1,2,2])
    print(result)