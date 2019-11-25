# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None and n > 1:
            return None
        node = ListNode(0)
        node.next = head
        first = node
        second = node
        while n:
            first = first.next
            n -= 1
        tmp = None
        while first:
            first = first.next
            tmp = second
            second = second.next


        tmp.next = tmp.next.next
        return node.next

