class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            ind = ord(char) - ord('a')
            if curr.children[ind] is None:
                curr.children[ind] = TrieNode()
            curr = curr.children[ind]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            ind = ord(char) - ord('a')
            if curr.children[ind] is None:
                return False
            curr = curr.children[ind]
        # curr.is_end = True
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for char in prefix:
            ind = ord(char) - ord('a')
            if curr.children[ind] is None:
                return False
            curr = curr.children[ind]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)