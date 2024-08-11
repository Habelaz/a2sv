class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def first(left,right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid -1] != target:
                        return mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid +  1
                else:
                    right = mid - 1
            return -1

        def last(left,right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid +  1
                else:
                    right = mid - 1
            return -1

        left,right = 0,len(nums) - 1
        return [first(left,right),last(left,right)]