class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c for c in s if c.isalpha() or c.isdigit()])
        i, j = 0, len(s) - 1
        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    solution = Solution()
    res = solution.isPalindrome("00")
    print(res)