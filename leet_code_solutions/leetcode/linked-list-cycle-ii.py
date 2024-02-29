# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        check = set()

        while curr:
            if curr not in check:
                
                check.add(curr)
                curr = curr.next
            else:
                return curr
            