class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # graph = defaultdict(list)
        # for a,b in edges:
        #     graph[a].append(b)
        #     graph[b].append(a)
        rank = [0] * (len(edges)+1)
        parent = [i for i in range(len(edges)+1)]
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
                elif rank[parent2] > rank[parent1]:
                    parent[parent1] = parent2

                else:
                    parent[parent2] = parent1
                    rank[parent1] += 1
                return 0
            else:
                return [node1,node2]
        
        
            

        for a,b in edges:
            found = union(a,b)
            if found :
                return found


