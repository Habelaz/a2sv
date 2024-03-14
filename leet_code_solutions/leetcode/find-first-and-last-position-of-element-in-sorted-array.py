class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # l,r = 0,len(nums)-1
        def first(nums,l,r):
            while l <= r:
                mid = (l+r) //2
                if nums[mid] == target:
                    if mid == 0 or nums[mid-1] != target:
                        return mid
                    else:
                        r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        def last(nums,l,r):
            while l <= r:
                mid = (l+r) //2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid+1] != target:
                        return mid
                    else:
                        l = mid +1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        return [first(nums,0,len(nums)-1),last(nums,0,len(nums)-1)]
        
