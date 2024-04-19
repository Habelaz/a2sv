# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        for i, li in enumerate(lists):
            if li: 
                heappush(heap, (li.val, i, li))
        print(heap)
        cur = dummy
        while heap:
            ntn, i, li = heappop(heap)
            if li.next:
                heappush(heap, (li.next.val, i, li.next))

            cur.next, cur = li, li

        return dummy.next
        