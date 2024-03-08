class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        stack = []
        ans = 0

        for i in range(len(arr)+1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                ind = stack.pop()
                left = stack[-1] if stack else -1
                right = i

                ans +=( arr[ind]* (ind - left) * (right - ind)) % mod
                ans %= mod
            stack.append(i)
        return ans