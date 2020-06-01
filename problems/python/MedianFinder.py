from heapq import heappush, heappushpop


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        else:
            return self.large[0]


if __name__ == "__main__":
    obj = MedianFinder()

    obj.addNum(1)
    obj.addNum(2)
    obj.findMedian()
    obj.addNum(3)
    obj.findMedian()
