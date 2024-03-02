# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        arr = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        # print(arr)
        def build(left,right):
            if left > right:
                return
            mid = (left+right)//2
            root = TreeNode(arr[mid])
            root.left = build(left,mid-1)
            root.right = build(mid+1,right)
            return root
        return build(0,len(arr)-1)                