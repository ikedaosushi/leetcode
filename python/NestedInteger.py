class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.data = nestedList
        self.cur = -1
        self.inneriter = None

    def next(self) -> int:
        if self.inneriter:
            return self.inneriter.next()
        return self.data[self.cur].getInteger()

    def hasNext(self) -> bool:
        if self.inneriter and self.inneriter.hasNext():
            return True
        self.inneriter = None
        if self.cur == len(self.data) - 1:
            return False

        self.cur += 1
        if self.data[self.cur].isInteger():
            return True
        self.inneriter = NestedIterator(self.data[self.cur].getList())
        if self.inneriter.hasNext():
            return True

        return self.hasNext()

        # Your NestedIterator object will be instantiated and called as such:
        # i, v = NestedIterator(nestedList), []
        # while i.hasNext(): v.append(i.next())

        # [[1,1],2,[1,1]] -> [1,1,2,1,1]
        # [1,[4,[6]]] -> [1,4,6]
