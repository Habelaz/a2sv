# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def sortt(nums):
            if not len(nums):
                return None
            ma = max(nums)
            ind = nums.index(ma)
            root = TreeNode(ma)
            
            root.left = sortt(nums[:ind])
            root.right = sortt(nums[ind+1:])

            return root
        return sortt(nums)