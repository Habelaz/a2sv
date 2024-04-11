class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for a,b in redEdges:
            red[a].append(b)
        for a,b in blueEdges:
            blue[a].append(b)
        answer = [-1] * n
        q = deque() 
        q.append([0,0,None])
        visited = set((0,None))
        # dist = 0
        
        while q:
            node,length,edgecolor = q.popleft()
            if answer[node] == -1:
                answer[node] = length

            if edgecolor != 'red':
                for neigh in red[node]:
                    if (neigh,'red') not in visited:
                        visited.add((neigh,'red'))
                        q.append((neigh,length+1,'red'))

            if edgecolor != 'blue':
                for neigh in blue[node]:
                    if (neigh,'blue') not in visited:
                        visited.add((neigh,'blue'))
                        q.append((neigh,length+1,'blue'))
            # dist += 1

        return answer