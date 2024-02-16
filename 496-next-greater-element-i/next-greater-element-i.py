class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapp = defaultdict(lambda :-1)

        for n in nums2:
            while stack and stack[-1] < n:
                x = stack.pop()
                mapp[x] = n
            stack.append(n) 
        # ans = []
        # for i in nums1:
        #     ans.append(mapp[i])
        # return ans
        return [mapp[val] for val in nums1]