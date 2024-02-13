# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        leftHead = left = ListNode()
        rightHead = right = ListNode()
        
        while curr:
            if curr.val < x:
                # print(curr.val)
                left.next = curr
                left = left.next
                
            else:
                right.next = curr
                right = right.next
        
            curr = curr.next
        # print(less)
            left.next = rightHead.next
            right.next = None
        return leftHead.next
        
        

        
        