# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root,val):
            if not root:
                return root

            if root.val > val:
                root.left = delete(root.left,val)
                return root
            elif root.val < val:
                root.right = delete(root.right,val)
                return root

            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left

            root.val = temp.val
            root.right = delete(root.right,root.val)
            return root
        
        return delete(root,key)

        