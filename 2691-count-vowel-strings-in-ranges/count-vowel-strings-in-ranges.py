class Solution:
    def vowelStrings(
        self, words: List[str], queries: List[List[int]]
    ) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        prefix_sum = [0] * (len(words) + 1)

        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                prefix_sum[i + 1] += 1
        
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i -1]
       
        return [prefix_sum[j + 1] - prefix_sum[i] for i, j in queries ]
