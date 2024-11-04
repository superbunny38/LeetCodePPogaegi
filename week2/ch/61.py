# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return
        else:
            size = 1
            cur = head
            while cur:
                if cur.next == None:
                    last = cur
                    break
                cur = cur.next
                size += 1
                
            last.next = head
            k = k%size

            cur = head
            for i in range(size-k):
                cur = cur.next
            new_start = cur
            for _ in range(size-1):
                cur = cur.next
            cur.next = None
            
            return new_start
