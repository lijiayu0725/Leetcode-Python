from typing import *

class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) == 0 or len(s) == 1:
            return
        for i in range(len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
