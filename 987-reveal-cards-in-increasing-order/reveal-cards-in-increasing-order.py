class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deq = deque(sorted(deck))
        ans = deque()
        n = len(deck)
        while n != len(ans):
            temp = deq.pop()
            if len(ans) > 0:
                r = ans.pop()
                ans.appendleft(r)
            ans.appendleft(temp)
        return ans