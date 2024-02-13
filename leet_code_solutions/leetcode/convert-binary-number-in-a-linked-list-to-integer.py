# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        for i in range(count-1,-1,-1):
            ans += head.val * (2**i)
            head = head.next

        return ans
        