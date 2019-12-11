from typing import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s not in ['+', '-', '*', '/']:
                stack.append(int(s))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if s == '+':
                    stack.append(num2 + num1)
                elif s == '-':
                    stack.append(num2 - num1)
                elif s == '*':
                    stack.append(num2 * num1)
                else:
                    stack.append(int(num2 / num1))
        return stack[0]


if __name__ == '__main__':
    solution = Solution()
    res = solution.evalRPN(["4", "13", "5", "/", "+"])
    print(res)
