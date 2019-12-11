from typing import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort()
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for nums in intervals[1:]:
            if nums[0] <= end and nums[1] >= end:
                end = nums[1]
            elif nums[0] >= start and nums[1] <= end:
                continue
            else:
                res.append([start, end])
                start = nums[0]
                end = nums[1]
        res.append([start, end])
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.merge([[1, 4], [2, 3]])
    print(res)
