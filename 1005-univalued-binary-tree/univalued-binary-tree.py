# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        traverse = []
        q = deque([root])

        while q:
            node = q.popleft()
            traverse.append(node.val)

            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        # print(traverse)
        return  len(set(traverse)) == 1