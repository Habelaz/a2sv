# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        x = root.val
        que = deque([root])
        # visited = set(root.val)
        # li = []

        
        while que:
            node = que.popleft()
            # li.append(value)
            if node.val != x:
                return False
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        return True
        

                
            

        



            