class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        colors = [0 for i in range(numCourses)]

        for course,pre in prerequisites:
            graph[pre].append(course)

        order = []
        def dfs(node):
            if colors[node] == 1:
                return False
            
            colors[node] = 1
            for nbr in graph[node]:
                if colors[nbr] == 2:
                    continue
                found = dfs(nbr)
                if not found:
                    return False

            colors[node] = 2
            order.append(node)
            return True
        for i in range(numCourses):
            if colors[i] != 0:
                continue
            
            if not dfs(i):
                return []
        return reversed(order)

        

        