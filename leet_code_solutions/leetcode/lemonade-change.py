class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twenties = 0
        # flag = False
        for i in range(len(bills)):
            if bills[i] == 5:
                fives += 1
            if bills[i] == 10:
                tens += 1
                if fives > 0:
                    fives -= 1
                else:
                    return False
            if bills[i] == 20:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False

        return True

                