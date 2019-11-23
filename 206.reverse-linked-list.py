# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            return head
        first = head
        second = head.next
        first.next = None
        while second:
            tmp = second.next
            second.next = first
            first = second
            second = tmp
        return first