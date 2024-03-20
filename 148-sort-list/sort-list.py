# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        curr = head

        while curr:
            nums.append(curr.val)
            curr = curr.next
        nums.sort()
        new_head = None
        current = None

        for val in nums:
            if not new_head:
                new_head = ListNode(val)
                current = new_head
            else:
                current.next = ListNode(val)
                current = current.next
        return new_head