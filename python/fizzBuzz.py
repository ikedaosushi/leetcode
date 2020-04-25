from typing import List


class Solution:
    def _fizzBuzz(self, number):
        if number % 15 == 0:
            return "FizzBuzz"
        elif number % 5 == 0:
            return "Buzz"
        elif number % 3 == 0:
            return "Fizz"
        else:
            return str(number)

    def fizzBuzz(self, n: int) -> List[str]:
        return [self._fizzBuzz(i) for i in range(1, n + 1)]
