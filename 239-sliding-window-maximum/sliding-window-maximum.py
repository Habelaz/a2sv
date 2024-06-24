class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        l = 0

        for r in range(len(nums)):

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            if (r + 1) >= k:
                ans.append(nums[q[0]])
                l += 1
            
            if l > q[0]:
                q.popleft()
            
        return ans