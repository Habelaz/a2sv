class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        j = 0
        ans = []
        processorTime.sort()
        tasks.sort(reverse = True)
        for i in range(len(processorTime)):
            ans.append(processorTime[i]+tasks[j])
            j += 4
        return max(ans)