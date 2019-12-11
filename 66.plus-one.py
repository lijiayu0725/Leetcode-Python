from typing import *


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return [1]
        pointer = len(digits) - 1
        while pointer >= 0 and digits[pointer] == 9:
            digits[pointer] = 0
            pointer -= 1
        if pointer == len(digits) - 1:
            digits[pointer] += 1
            return digits
        else:
            if pointer < 0:
                digits.insert(0, 1)
                return digits
            else:
                digits[pointer] += 1
            return digits
