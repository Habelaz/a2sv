# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = 0
        def maxSum(root):
            le, lemin, lemax = maxSum(root.left) if root.left else (0, float('inf'), float('-inf'))
            ri, rimin, rimax = maxSum(root.right) if root.right else (0, float('inf'), float('-inf'))
            if le is not None  and ri is not None:
                if root.val > lemax and root.val < rimin:
                    summ = root.val + le + ri
                    self.ans = max(self.ans, summ)
                    return summ, min(root.val, lemin), max(root.val, rimax)
            return (None, None, None)
        maxSum(root)
        return self.ans

        