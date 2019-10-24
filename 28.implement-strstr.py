class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if i + j >= len(haystack):
                    return -1
                if haystack[i + j] == needle[j]:
                    if j + 1 == len(needle):
                        return i
                    continue
                else:
                    break
        return -1


if __name__ == '__main__':
    solution = Solution()
    result = solution.strStr('aaaa', 'aaa')
    print(result)