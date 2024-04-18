class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]

        for course,pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
        q = deque()
        for c,inc in enumerate(incoming):
            if inc == 0:
                q.append(c)
        order = []
        while q:
        
            node = q.popleft()
            order.append(node)
            for nbr in graph[node]:
                incoming[nbr] -= 1

                if incoming[nbr] == 0:
                    q.append(nbr)
        if len(order) != numCourses:
            return []

        return order

        