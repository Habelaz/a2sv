# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        arr = []
        while current:
            arr.append(current.val)
            current = current.next
        arr.sort()
        new_head = None
        current = None

        for val in arr:
            if not new_head:
                new_head = ListNode(val)
                current = new_head
            else:
                current.next = ListNode(val)
                current = current.next
        return new_head