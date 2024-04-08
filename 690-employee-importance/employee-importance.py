"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        stack = [id]
        graph = defaultdict(list)

        for e in employees:
            graph[e.id] = e

        ans  = 0
        while stack:
            e_id = stack.pop()
            e = graph[e_id]
            ans += e.importance

            for sub in e.subordinates:
                stack.append(sub)

        return ans

