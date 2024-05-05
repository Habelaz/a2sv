class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]
        rank = [0] * (n+1)

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        def union(node1,node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 != parent2:
                if rank[parent1] > rank[parent2]:
                    parent[parent2] = parent1
                elif rank[parent1] < rank[parent2]:
                    parent[parent1] = parent2
                else:
                    parent[parent2] = parent1
                    rank[parent1] += 1
                

        for a,b,dist in roads:
            union(a,b)

        min_d = float('inf')
        for a,b,dist in roads:
            if find(a) == find(n):
                min_d = min(min_d,dist)

        return min_d