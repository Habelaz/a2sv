class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        visited = {''}
        ans = ''

        for w in words:
            if w[:-1] in visited:
                visited.add(w)
                if len(w) > len(ans):
                    ans = w

        return ans