class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        masks = [0] * len(words)

        for i in range(len(words)):
            curr = 0

            for s in words[i]:
                curr |= 1 << (ord(s) - ord('a'))
            
            masks[i] = curr

        max_length = 0
        for i in range(len(masks)):
            for j in range(i+1,len(masks)):
                if masks[i] & masks[j] == 0:
                    max_length = max(max_length,len(words[i])*len(words[j]))
        return max_length