# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = {}
        self.max_diff = 0
        def max_width(root, ind, level, d):
            if root is None:
                return 
            d.setdefault(level, [ind, ind])
            d[level][0] = min(d[level][0], ind)
            d[level][1] = max(d[level][1], ind)
            self.max_diff = max(self.max_diff, d[level][1] - d[level][0])

            max_width(root.left, 2*ind, level+1, d)
            max_width(root.right, 2*ind+1, level+1, d)
        max_width(root, 0, 0, d)
        return self.max_diff+1