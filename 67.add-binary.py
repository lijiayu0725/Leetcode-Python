class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        a.reverse()
        b.reverse()
        i = 0
        carry = 0
        res = []
        while i < len(a) or i < len(b):
            num_a = int(a[i]) if i < len(a) else 0
            num_b = int(b[i]) if i < len(b) else 0
            total = num_a + num_b
            num = (total + carry) % 2
            carry = (total + carry) // 2
            res.append(str(num))
            i += 1
        if carry != 0:
            res.append(str(carry))
        return ''.join(reversed(res))


if __name__ == '__main__':
    solution = Solution()
    res = solution.addBinary('0', '1')
    print(res)
