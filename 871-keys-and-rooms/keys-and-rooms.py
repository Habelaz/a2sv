class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        q = deque()
        q.append(0)

        while q:
            room = q.popleft()
            for k in rooms[room]:
                if not visited[k]:
                    visited[k] = True
                    q.append(k)
        # visited = set(visited)
        # return not(False in visited)
        return all(visited)
        


        