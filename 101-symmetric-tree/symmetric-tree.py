# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmetric(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            left_tr = symmetric(left.left,right.right)
            right_tr = symmetric(left.right,right.left)
            return left.val == right.val and left_tr and right_tr
        
        return symmetric(root.left,root.right)