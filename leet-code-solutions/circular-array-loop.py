class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False

        seen = set()
        for i in range(n):
            if i not in seen:
                cycle = set()
                while True:
                    if i in cycle:
                        return True
                    seen.add(i)
                    cycle.add(i)
                    prev, i = i, (i + nums[i]) % n

                    if prev == i:
                        break

                    if nums[prev] > 0 != nums[i] < 0:
                        break

        return False
                

        