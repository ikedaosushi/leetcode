class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append((x, min(self._getMin(), x)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def _getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return float('inf')

    def getMin(self) -> int:
        if self.stack:
            return self._getMin()
