from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = SortedList()
        ans = []
        nums.reverse()
        for num in nums:
            ind = bisect.bisect_left(s,num)
            ans.append(ind)
            s.add(num)

        return reversed(ans)