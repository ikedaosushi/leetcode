from typing import List
from collections import deque


class Solution:
    def get_neighbors_dic(self, wordList):
        d = {}
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]
                d[s] = d.get(s, []) + [word]
        return d

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbors_dic = self.get_neighbors_dic(
            set(wordList) | set([beginWord, endWord]))

        # print(f"neighbors_dic: {neighbors_dic}")

        queue, visited = deque([(beginWord, 1)]), set()
        while queue:
            word, step = queue.popleft()
            # print(f"word: {word}, queue: {queue}")
            if word in visited:
                continue
            visited.add(word)

            if word == endWord:
                return step

            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]
                neighbors = neighbors_dic.get(s, [])
                # print(f"s: {s}, neighbors: {neighbors}")
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append((neighbor, step + 1))
            # print(f"queue: {queue}")

        return 0
