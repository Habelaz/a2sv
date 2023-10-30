class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        ans = []
        target = sorted(p)  # Sort the target string to compare with later

        for i in range(len(s) - k + 1): 
            window = sorted(s[i:i+k])  
            if window == target:  
                ans.append(i)

        return ans