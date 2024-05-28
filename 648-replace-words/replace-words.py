
class Trie:
    def __init__ (self):
        self.root = {}

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['*'] = {}

    def search(self, word):
        curr = self.root
        succ = ''
        for c in word:
            if c not in curr:
                break
            curr = curr[c]
            succ += c
            if '*' in curr: return succ
        return word
        

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        ans = []
        sentence = sentence.split()

        for s in sentence:
            ans.append(trie.search(s))

        return ' '.join(ans)
