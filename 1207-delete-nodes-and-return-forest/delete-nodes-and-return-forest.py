# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        def dfs(root):
            if not root:
                return None

            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if root.val in to_delete:
                if not root.left and not root.right:
                    return None

                if root.left:
                    ans.append(root.left)
                if root.right:
                    ans.append(root.right)
                return None

            return root
            
        to_delete = set(to_delete)
        node = dfs(root)
        if node:
            ans.append(node)
        return ans

                
