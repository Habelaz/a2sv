class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # if target <= startValue:
        #     return startValue - target
        oper = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            oper += 1
        return oper + startValue - target
        