class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u,v in prerequisites:
            graph[v].append(u)
        
        WHITE = 1
        GREY = 2
        BLACK = 3

        color = [WHITE for i in range(numCourses)]

        def dfs(node):
            color[node] = GREY

            for neighbour in graph[node]:
                if color[neighbour] == GREY:
                    return False
                elif color[neighbour] == WHITE:
                    found = dfs(neighbour)
                    if not found:
                        return False
            color[node] = BLACK
            return True

        for course in range(numCourses):
            if color[course] == WHITE:
                if not dfs(course):
                    return False
    
        return True



            