# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        x = list(reversed(arr[left-1:right]))
        # print(x)
        arr = arr[:left-1] + x + arr[right:]
        new_head = None
        curr = None

        for val in arr:
            if not new_head:
                new_head = ListNode(val)
                curr = new_head
            else:
                curr.next = ListNode(val)
                curr = curr.next
        return new_head