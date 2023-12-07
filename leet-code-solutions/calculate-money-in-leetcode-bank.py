class Solution:
    def totalMoney(self, n: int) -> int:
        savings=[1,2,3,4,5,6,7]
        money = 0
        for i in range(n):
            money += savings[i%7]
            savings[i%7] += 1
        return money
            