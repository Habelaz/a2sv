# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            left = root.left
            right = root.right
            if not root.left or not root.right:
                return max(dfs(left),dfs(right)) + 1
                
            return  min(dfs(left),dfs(right)) + 1
        return dfs(root)
                
            