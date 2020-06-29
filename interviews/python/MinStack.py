class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        currentMin = self.getMin()
        if currentMin is None or x < currentMin:
            currentMin = x
        self.q.append((x, currentMin))

    def pop(self) -> None:
        if len(self.q) == 0:
            return None
        else:
            return self.q.pop()

    def top(self) -> int:
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][0]

    def getMin(self) -> int:
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
