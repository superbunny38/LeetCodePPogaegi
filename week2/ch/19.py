# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
 
        dummy = ListNode()
        dummy.next = head
        
        f = dummy
        s = dummy

        for _ in range(n):
            f = f.next
        
        while f.next:
            f = f.next
            s = s.next
        
        s.next = s.next.next

        return dummy.next
