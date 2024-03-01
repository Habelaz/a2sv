# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        main_len = length // k
        rem = length % k

        res = []
        curr = head
        for i in range(k):
            res.append(curr)

            for j in range(main_len -1 + (1 if rem else 0)):
                if not curr:
                    break
                curr = curr.next
            if rem > 0:
                rem -= 1
            if curr:
                curr.next,curr = None,curr.next
        return res
