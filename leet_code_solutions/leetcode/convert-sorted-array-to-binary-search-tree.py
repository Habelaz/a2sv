# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        left = 0
        right = len(nums) - 1
        def sortt(nums):
            if not len(nums):
                return None
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = sortt(nums[:mid])
            root.right = sortt(nums[mid+1:])

            return root
        return sortt(nums)



        