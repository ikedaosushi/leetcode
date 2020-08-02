class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_ = []

    def add(self, key: int) -> None:
        if key not in self.hash_:
            self.hash_.append(key)

    def remove(self, key: int) -> None:
        if key in self.hash_:
            for i, k in enumerate(self.hash_):
                if k == key:
                    self.hash_.pop(i)
                    break

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.hash_


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
