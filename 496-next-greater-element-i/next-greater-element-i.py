class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        maxx = max(nums1) + 1
        greater = defaultdict(lambda : -1)

        for n in nums2:
            while stack and stack[-1] < n:
                greater[stack.pop()] = n 
            stack.append(n)
        
        return [greater[n] for n in nums1]
