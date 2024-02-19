class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sec = 0

        while True:
            for i in range(len(tickets)):
                if tickets[i] != 0:
                    tickets[i] -= 1

                    sec += 1

                if i == k and tickets[k] == 0:
                    return sec
        
        
            
            
