class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = [i for i in range(len(stones))]
        rank = [0] * len(stones)

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        def union(node1,node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return 0
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
            elif rank[parent1] < rank[parent2]:
                parent[parent1] = parent2
            else:
                parent[parent2] = parent1
                rank[parent1] += 1
            return 1
        
        ans = 0
        rows,cols ={},{}

        for i,(r,c) in enumerate(stones):
            if r in rows:
                ans += union(i,rows[r])
            rows[r] = i
            if c in cols:
                ans += union(i,cols[c])
            cols[c] = i
        
        return ans