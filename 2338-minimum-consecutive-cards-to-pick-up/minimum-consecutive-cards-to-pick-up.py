class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_l = len(cards) + 1
        l = 0
        ans = set()
        for r in range(len(cards)):

            while cards[r] in ans:
                min_l = min(min_l,r-l+1)
                ans.remove(cards[l])
                l += 1
            ans.add(cards[r])
        if min_l == len(cards) + 1:
            return -1
        return min_l