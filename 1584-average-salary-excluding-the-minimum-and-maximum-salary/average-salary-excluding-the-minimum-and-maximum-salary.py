class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        newS=salary[1:-1]
        n=len(newS)
        average = sum(newS)/n
        return average
        