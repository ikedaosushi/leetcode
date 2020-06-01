import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.vals:
            return False
        self.vals[val] = True
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.vals:
            return False
        del self.vals[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return list(self.vals.keys())[random.randint(0, len(self.vals) - 1)]
