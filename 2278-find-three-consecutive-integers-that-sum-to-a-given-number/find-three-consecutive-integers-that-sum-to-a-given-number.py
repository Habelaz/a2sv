class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        x=num//3
        # for i in range(3):
        total = x + x - 1 + x + 1
        if total == num:
            return [x-1,x,x+1]
        else:
            return []
