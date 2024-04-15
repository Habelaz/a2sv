class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if '0000' in visited:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                char = str((int(lock[i])+1)%10)
                res.append(lock[:i] + char + lock[i+1:])
                char = str((int(lock[i])+9)%10)
                res.append(lock[:i] + char + lock[i+1:])
            return res

        q = deque()
        q.append(['0000',0])
        while q:
            for i in range(len(q)):
                lock,turns = q.popleft()

                if lock == target:
                    return turns
                graph = children(lock)
                for child in graph:
                    if child not in visited:
                        visited.add(child)
                        q.append([child,turns + 1])
        return -1