class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        self.count = 0

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
            curr.count += 1
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        total = 0
        for char in word:
            ind = ord(char) - ord('a')
            if curr.children[ind] is None:
                return total
            curr = curr.children[ind]
            total += curr.count
        return total
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for w in words:
            trie.insert(w)

        ans = []
        for w in words:
            ans.append(trie.search(w))
        return ans