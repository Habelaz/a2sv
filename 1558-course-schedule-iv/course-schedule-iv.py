class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not prerequisites:
            return [False] * len(queries)
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        pre_q = defaultdict(set)
        for pre,course in prerequisites:
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
                pre_q[nbr].add(node)
                pre_q[nbr].update(pre_q[node])
                incoming[nbr] -= 1

                if incoming[nbr] == 0:
                    q.append(nbr)
        if len(order) != numCourses:
            return []
        
        ans = []
        for a,b in queries:
            if a in pre_q[b]:
                ans.append(True)
            else:
                ans.append(False)
        return ans