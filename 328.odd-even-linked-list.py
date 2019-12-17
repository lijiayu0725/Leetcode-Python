# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        oddhead = head
        evenhead = head.next
        tmp_even = evenhead
        while oddhead and oddhead.next:
            oddhead.next = evenhead.next
            oddhead = oddhead.next
            evenhead.next = oddhead.next
            evenhead = evenhead.next
        oddhead.next = tmp_even
        return head
