class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if s == '':
            return 0
        sum = ROMAN[s[-1]]
        for i in reversed(range(len(s) - 1)):
            if ROMAN[s[i + 1]] > ROMAN[s[i]]:
                sum -= ROMAN[s[i]]
            else:
                sum += ROMAN[s[i]]
        return sum