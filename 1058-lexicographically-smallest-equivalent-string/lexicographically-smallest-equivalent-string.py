class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = { chr(c):chr(c) for c in range(ord('a'),ord('z')+1) }
        

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for i in range(len(s1)):
            node1 = find(s1[i])
            node2 = find(s2[i])
            if node1 > node2:
                parent[node1] = node2
            else:
                parent[node2] = node1

        ans = ''
        for c in baseStr:
            ans += find(c)

        return ans


        
        
        
            