class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store1 = Counter(nums1)
        store2 = Counter(nums2)
        ans = []
        for key in store1:
            if key in store2:
                ans += [key] * min(store1[key],store2[key])
        return ans

        