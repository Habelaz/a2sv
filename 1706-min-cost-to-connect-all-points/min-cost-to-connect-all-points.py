class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = [i for i in range(len(points))]
        rank = [0 for i in range(len(points))]
        
        def distance(pt1,pt2):
            return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])
        
        dist = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                d = distance(points[i],points[j])
                dist.append((d,i,j))

        dist.sort()

        

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(node1,node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return False
            else:
                if rank[parent1] > rank[parent2]:
                    parent[parent2] = parent1
                elif rank[parent1] < rank[parent2]:
                    parent[parent1] = parent2
                else:
                    parent[parent2] = parent1
                    rank[parent1] += 1
                return True
        length = 0
        nodes = 0
        for d,pt1,pt2 in dist:
            if union(pt1,pt2):
                length += d
                nodes += 1

            if nodes == len(points) - 1:
                break
        return length

