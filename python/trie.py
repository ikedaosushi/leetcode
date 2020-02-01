class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.has_end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)
            current = current.children[letter]
        current.has_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.has_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
