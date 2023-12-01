class Solution:
    def freqAlphabets(self, s: str) -> str:
        map_ai={'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i'}
        map_jz={'10#':'j','11#':'k','12#':'l','13#':'m','14#':'n','15#':'o','16#':'p','17#':'q','18#':'r','19#':'s','20#':'t','21#':'u','22#':'v','23#':'w','24#':'x','25#':'y','26#':'z'}
        myList=[]
        # i = 0
        # while i < len(s):
        #     if i+2 < len(s):
        #         if s[i+2] == '#':
        #             x = s[i:i+3]
        #             myList.append(map_jz[x])
        #             i += 3
        #     else:
        #         myList.append(map_ai[s[i]])
        #         i += 1
        
        # return ''.join(myList)
        s=s[::-1]
        i = 0
        while i < len(s):
            if s[i] == '#':
                x=s[i:i+3]
                x=x[::-1]
                myList.append(map_jz[x])
                i += 3
            else:
                myList.append(map_ai[s[i]])
                i += 1
        ans=''.join(myList)
        return ans[::-1]