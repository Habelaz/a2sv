"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def order(node):
            if not node:
                return
            for child in node.children:
                order(child)
            ans.append(node.val)

        order(root)
        return ans