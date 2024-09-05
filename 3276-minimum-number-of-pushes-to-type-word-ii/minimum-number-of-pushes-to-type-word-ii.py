class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        freq = list(counts.values())
        # print(freq)
        freq.sort(reverse = True)

        ans = 0
        distinct = 0
        for c in freq:
            ans += c * (1 + distinct // 8)
            distinct += 1

        return ans
