from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if len([a for a in arr if a == 0]) == 2:
            return True
        hash_ = {k: 0 for k in arr}
        for n in arr:
            if n != 0 and n * 2 in hash_:
                return True

        return False
