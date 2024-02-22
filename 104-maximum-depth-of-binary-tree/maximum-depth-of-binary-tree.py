# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # count = 0
        def maxd(root):
            if not root:
                return 0
            
            left_depth = maxd(root.left)
            right_depth = maxd(root.right)

            if left_depth < right_depth:
                return right_depth + 1
            else:
                return left_depth + 1
        return maxd(root)