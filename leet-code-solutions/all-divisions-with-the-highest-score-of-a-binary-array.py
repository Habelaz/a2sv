class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        summ = sum(nums)
        leftSum = 0
        rightSum = summ
        maxx = summ
        indices = [0]
        for i in range(len(nums)):
            if nums[i] == 0:
                leftSum += 1
            else:
                rightSum -= 1
            score = leftSum + rightSum
            if score == maxx:
                indices.append(i+1)
                continue
            elif score > maxx:
                maxx = score
                indices = [i+1]
        return indices
            
