# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root,p,q):
            if not root:
                return 
            if q.val < root.val and p.val < root.val:
                return lca(root.left,p,q)
            if q.val > root.val and p.val > root.val:
                return lca(root.right,p,q)
            else:
                return root
            # if root.left == p or root.right == q:
            #     return root

        return lca(root,p,q)