from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ''
        for middle in range(len(s)):
            tmp = self.find_max_len(s, middle, middle)
            max_str = tmp if len(tmp) > len(max_str) else max_str
            tmp = self.find_max_len(s, middle, middle + 1)
            max_str = tmp if len(tmp) > len(max_str) else max_str
        return max_str


    def find_max_len(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]