from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        unique = set()
        longest = 0
        for i in range(len(s)):
            while j < len(s) and s[j] not in unique:
                unique.add(s[j])
                j += 1
            longest = max(longest, j - i)
            unique.remove(s[i])
        return longest