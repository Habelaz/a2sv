# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        ans = []
        q = deque([(root,None,0)])

        while q:
            for i in range(len(q)):
                node,parent,depth = q.popleft()
                if len(ans) == 2:
                    break
                if node.val == x or node.val == y:
                    ans.append([parent,depth])
                if node.left:
                    q.append((node.left,node,depth + 1))
                if node.right:
                    q.append((node.right,node,depth+1))

        one,two = ans

        return one[1] == two[1] and one[0] != two[0]
        