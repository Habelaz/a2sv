# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = [root]
        ans = [[root.val]]

        while level:
            
            nextlevel = []
            temp = []
            for node in level:
                if node.left:
                    nextlevel.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    nextlevel.append(node.right)
                    temp.append(node.right.val)
            if temp:
                ans.append(temp)
            level = nextlevel

        return ans