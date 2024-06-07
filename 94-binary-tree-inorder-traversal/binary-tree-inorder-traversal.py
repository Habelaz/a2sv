# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preorder(root):
            if not root:
                return
            # print("left:",root.left, "value :",root.val,'right :',root.right)
            preorder(root.left)
            ans.append(root.val)
            preorder(root.right)
            return ans
        
        return preorder(root)