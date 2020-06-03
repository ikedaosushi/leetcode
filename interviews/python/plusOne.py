from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            tmp = digits[i] + 1 + carry
            if tmp >= 10:
                digits[i] = 0
                carry = tmp - 10
            else:
                digits[i] = tmp
                return digits

        return [1] * 1 + digits
