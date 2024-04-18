class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        heap = []

        for key,val in freq.items():
            heappush(heap,(val,key))
        sorted_freq = nlargest(k,heap)
        ans = []
        for val,key in sorted_freq:
            ans.append(key)
        return ans