class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        window = {}

        have,need = 0,len(count_t)
        res = [0,0]
        reslen = float('inf')

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1

            if window[s[r]] == count_t[s[r]]:
                have += 1

            while have == need:
                if r-l+1 < reslen:
                    res = [l,r]
                    reslen = r-l+1
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]: 
                    have -= 1
                l += 1

        l,r = res
        if reslen == float('inf'):
            return ''
        return s[l:r+1]      
            