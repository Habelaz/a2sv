class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        sh =[0] * (len(s)+1)
        for a,b,di in shifts:
            # di = shifts[i][2]
            # a = shifts[i][0]
            # b = shifts[i][1]
            if di == 0:
                sh[a] -= 1
                sh[b+1] += 1
            else:
                sh[a] += 1
                sh[b+1] -= 1
        
        acc = 0
        for i in range(len(sh)):
            acc += sh[i]
            sh[i] = acc

        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        ans = ''
        for i,c in enumerate(s):
            ind = alpha.index(s[i]) + sh[i]
            ans += alpha[ind%26]

            # ind = (ord(c) - ord('a') + sh[i]) % 26
            # ans += chr(ind + ord('a'))
        
        return ans

