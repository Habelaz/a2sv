# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque([root])
        ans = []

        while que:
            ans.append([node.val for node in que])

            for _ in range(len(que)):
                node = que.popleft()
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                

        return ans
