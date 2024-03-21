class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # print(count)
        count_sorted = dict(sorted(count.items(), key=lambda d: d[1],reverse = True))
        # print(count_sorted)
        ans = []
        for a,b in count_sorted.items():
            ans.append(a)
            if len(ans) == k:
                return ans