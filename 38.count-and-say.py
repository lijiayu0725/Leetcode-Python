class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        num = 1
        n -= 1
        while n:
            num = self.say(num)
            n -= 1
        return num

    def say(self, num: int) -> str:
        num = str(num)
        count = 1
        res = ''
        for i in range(1, len(num)):
            if num[i] == num[i - 1]:
                count += 1
            else:
                res += str(count) + num[i - 1]
                count = 1
        res += str(count) + num[-1]
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.countAndSay(2)
    print(res)
