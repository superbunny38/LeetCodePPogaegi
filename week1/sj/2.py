# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        add_one = False
        while l1 or l2:
            new_val = 0
            if l1:
                new_val += l1.val
                l1 = l1.next
            if l2:
                new_val += l2.val
                l2 = l2.next
            if add_one:
                new_val += 1
                add_one = False
            if new_val >= 10:
                new_val -= 10
                add_one = True
            new_node = ListNode(new_val)
            nodes.append(new_node)
        if add_one:
            nodes.append(ListNode(1))
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]
