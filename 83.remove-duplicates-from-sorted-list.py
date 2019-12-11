# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        head_0 = ListNode(0)
        tmp = head_0
        head_0.next = head
        slow, fast = head, head
        while fast:
            if fast.val == slow.val:
                fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next
        if slow and slow.next and slow.val == slow.next.val:
            slow.next = None
        return tmp.next
