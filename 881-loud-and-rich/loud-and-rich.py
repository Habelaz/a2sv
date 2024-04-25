class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        inDegrees = [0] * n
        graph = defaultdict(list)
        for a, b in richer:
            graph[a].append(b)
            inDegrees[b] += 1

        res = [e for e in range(n)]
        quietest = quiet.copy()

        q = collections.deque([i for i, degree in enumerate(inDegrees) if degree == 0])

        while q:
            node = q.popleft()

            for out in graph[node]:
                if quiet[node] < quiet[out]:
                    quiet[out] = quiet[node]
                    res[out] = res[node]
                inDegrees[out] -= 1
                if inDegrees[out] == 0:
                    q.append(out)
        return res