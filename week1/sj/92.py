# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        prev, cur = None, head
        for _ in range(left - 1):
            prev = cur
            cur = cur.next
        reverse_begin, before_reverse = cur, prev
        temp = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        reverse_begin.next = cur
        if before_reverse:
            before_reverse.next = prev
            return head
        return prev
