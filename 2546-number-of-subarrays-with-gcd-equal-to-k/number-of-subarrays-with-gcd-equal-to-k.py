class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        if k == 1:
            for i in range(n):
                temp = nums[i]
                for j in range(i, n):
                    temp = math.gcd(temp, nums[j])
                    if temp == k:
                        count += 1
                    elif temp < k:
                        break
            return count
        l = 0
        arr = deque()
        for r in range(n):
            arr.append(nums[r])
            while math.gcd(*arr) !=  k and l < r:
                l += 1
                arr.popleft()
                
            count += (r-l)
        for n in nums:
            if n == k:
                count += 1

        return count 
            