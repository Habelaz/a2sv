# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def diff(root,minn,maxx):
            nonlocal ans

            if not root:
                return None
            if minn > root.val:
                minn = root.val
            if maxx < root.val:
                maxx = root.val

            ans = max(ans,abs(maxx-minn))

            diff(root.left,minn,maxx)
            diff(root.right,minn,maxx)

            return ans
        return diff(root,root.val,root.val)
        
        # return max(abs(refer - b),abs(refer - a))
            