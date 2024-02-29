# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mapp = defaultdict(int)

        def traverse(root):
            if not root:
                return
            mapp[root.val] += 1
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        ans = []
        vals = [val for key,val in mapp.items()]
        print(vals)
        maxx = max(vals)
        # print(maxVal)
        for key,val in mapp.items():
            if val == maxx:
                ans.append(key)
        return ans