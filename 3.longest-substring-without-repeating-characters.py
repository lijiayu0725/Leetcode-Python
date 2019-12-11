class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_count = 0
        cha = set()
        j = 0
        for i in range(len(s)):
            while j < len(s) and s[j] not in cha:
                cha.add(s[j])
                j += 1
            longest_count = max(longest_count, j - i)
            cha.remove(s[i])
        return longest_count
