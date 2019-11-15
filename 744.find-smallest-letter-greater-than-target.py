from typing import *

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if target > letters[mid]:
                start = mid
            elif target < letters[mid]:
                end = mid
            else:
                start = mid
        if letters[start] > target:
            return letters[start]
        if letters[end] > target:
            return letters[end]
        return letters[0]