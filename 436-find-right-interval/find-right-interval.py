class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        nums = sorted(intervals)
        starts = {}
        for i in range(len(intervals)):
            starts[intervals[i][0]] = i
        
        def fun(interval):
            low,high = 0,len(nums) - 1
            target = interval[1]
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid][0] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return starts[nums[low % len(nums)][0]] if nums[low % len(nums)][0] >= target else -1
            
        ans = []
        for i,interval in enumerate(intervals):
            ans.append(fun(interval))
        return ans
        
        
            