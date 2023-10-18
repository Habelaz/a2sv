class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        concat = ''.join(map(str, digits))
        concat=int(concat)
        concat += 1
        ans=[]
        for i in str(concat):
            ans.append(int(i))

        return ans


