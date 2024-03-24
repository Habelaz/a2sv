class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # l,r = 0,len(nums)-1
        def first(left,right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == 0 or  nums[mid - 1] != target:
                        return mid
                    else:
                        right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        def last(left,right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid+1] != target:
                        return mid
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        return [first(0,len(nums)-1),last(0,len(nums)-1)]
        
