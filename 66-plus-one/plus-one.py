class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # num = ''.join(map(str, digits))
        num = ''
        for i in digits:
            num += str(i)
        num=int(num)
        num += 1
        ans=[]
        for i in str(num):
            ans.append(int(i))

        return ans


