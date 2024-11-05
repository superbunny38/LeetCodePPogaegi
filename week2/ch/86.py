# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head

        dummy = ListNode(x-1)
        dummy.next = head
        fast_pointer = dummy.next
        slow_pointer = dummy
        pivot_left = None
        
        while fast_pointer:
            if fast_pointer.val >= x and pivot_left == None:
                pivot_left = slow_pointer
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next
                continue
            
            if pivot_left and fast_pointer.val <x:
                slow_pointer.next = fast_pointer.next#delete
                #insert
                fast_pointer.next = pivot_left.next
                pivot_left.next = fast_pointer
                pivot_left = pivot_left.next#move pivot
                fast_pointer = slow_pointer.next#relocate
                continue
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        
        return dummy.next
