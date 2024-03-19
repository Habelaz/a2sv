class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_half,right_half):
            ptr1,ptr2 = 0,0
            ans = []
            while ptr1 < len(left_half) and ptr2 < len(right_half):
                if left_half[ptr1] > right_half[ptr2]:
                    ans.append(right_half[ptr2])
                    ptr2 += 1
                else:
                    ans.append(left_half[ptr1])
                    ptr1 += 1
            ans.extend(left_half[ptr1:])
            ans.extend(right_half[ptr2:])

            return ans

        def mergesort(left,right,arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergesort(left,mid,arr)
            right_half = mergesort(mid+1,right,arr)

            return merge(left_half,right_half)
        
        return mergesort(0,len(nums)-1,nums)