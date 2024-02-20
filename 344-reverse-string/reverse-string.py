class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        def reverseS(s,l,r):
            if l >= r:
                return 
            s[l],s[r] = s[r],s[l]
            # print(s)
            return reverseS(s,l+1,r-1)
        reverseS(s,l,r)
            

