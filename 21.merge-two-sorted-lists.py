# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        final = ListNode(0)
        res = final
        first, second = l1, l2
        while first and second:
            if first.val <= second.val:
                final.next = first
                first = first.next
            else:
                final.next = second
                second = second.next
            final = final.next
        if first:
            final.next = first
        if second:
            final.next = second
        return res.next
