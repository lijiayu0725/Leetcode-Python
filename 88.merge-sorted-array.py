from typing import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = [0 for _ in range(m + n)]
        i, j, k = 0, 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                tmp[k] = nums1[i]
                i += 1
            else:
                tmp[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
            tmp[k] = nums1[i]
            i += 1
            k += 1
        while j < n:
            tmp[k] = nums2[j]
            j += 1
            k += 1
        for i in range(m + n):
            nums1[i] = tmp[i]
