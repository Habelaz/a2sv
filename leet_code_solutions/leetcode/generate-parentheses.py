class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        path = []
        def generate(open,close):
            if open == close == n:
                ans.append(''.join(path[:]))
                return

            if open < n:
                path.append('(')
                generate(open+1,close)
                path.pop()
            
            if open > close:
                path.append(')')
                generate(open,close+1)
                path.pop()
        generate(0,0)  
        return ans