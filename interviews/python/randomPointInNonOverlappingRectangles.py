from bisect import bisect_left
from random import randint
from typing import List


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects, self.ranges, sm = rects, [], 0
        for x1, y1, x2, y2 in rects:
            sm += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(sm)

    def pick(self) -> List[int]:
        x1, y1, x2, y2 = self.rects[bisect_left(
            self.ranges, randint(1, self.ranges[-1]))]
        return [randint(x1, x2), randint(y1, y2)]
