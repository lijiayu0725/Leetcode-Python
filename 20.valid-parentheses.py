class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                tmp = stack.pop()
                if tmp == '(' and c != ')':
                    return False
                elif tmp == '[' and c != ']':
                    return False
                elif tmp == '{' and c != '}':
                    return False
        return len(stack) == 0
