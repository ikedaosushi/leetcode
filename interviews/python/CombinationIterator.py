class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        def combi(cur, idx):
            if len(cur) == combinationLength:
                yield ''.join(cur)
                return
            for i in range(idx, len(characters)):
                cur.append(characters[i])
                yield from combi(cur, i + 1)
                cur.pop()
        self.combos = combi([], 0)
        self.current = True
        self.hasNextCalled = False

    def next(self) -> str:
        if self.hasNext():
            self.hasNextCalled = False
            return self.current

    def hasNext(self) -> bool:
        if self.current and not self.hasNextCalled:
            self.hasNextCalled = True
            self.current = next(self.combos, False)
        return bool(self.current)
