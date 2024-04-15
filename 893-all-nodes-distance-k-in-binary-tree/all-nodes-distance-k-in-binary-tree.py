class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        parent = {}
        q = deque()
        q.append(root)

        while q:
            
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    parent[node.left.val] = node
                    q.append(node.left)

                if node.right:
                    parent[node.right.val] = node
                    q.append(node.right)

        visited = {}
        q.append(target)
        while k > 0 and q:

            for _ in range(len(q)):
                node = q.popleft()

                visited[node.val] = 1

                if node.left and node.left.val not in visited:
                    q.append(node.left)

                if node.right and node.right.val not in visited:
                    q.append(node.right)

                if node.val in parent and parent[node.val].val not in visited:
                    q.append(parent[node.val])

            k -= 1

        while q:
            ans.append(q.popleft().val)

        return ans