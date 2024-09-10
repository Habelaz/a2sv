class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = [[d,p] for d,p in  zip(difficulty, profit)]
        jobs.sort()
        worker.sort()

        profitSum = 0
        maxProfit = 0
        j = 0

        for ability in worker:
            while j < len(jobs) and ability >= jobs[j][0]:
                maxProfit = max(maxProfit, jobs[j][1])
                j += 1
            profitSum += maxProfit

        return profitSum