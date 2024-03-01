# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        summ = []
        def traverse(root,num):
            nonlocal ans
            if not root:
                return
            if not root.left and not root.right:
                num += str(root.val)
                ans += int(num)
                # summ.append(num)
                # num = ''
                # print(ans,num)
            else:
                num += str(root.val)
            
                traverse(root.left,num)
                traverse(root.right,num)
        traverse(root,'')
        
        # for num in summ:
        #     ans += int(num)
        return ans
