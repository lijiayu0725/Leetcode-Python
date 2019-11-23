# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        addtion = 0
        head = ListNode(0)
        tmp = head
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = int((val1 + val2 + addtion) % 10)
            addtion = (val1 + val2 + addtion) / 10
            tmp.next = ListNode(sum)
            tmp = tmp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if int(addtion) != 0:
            tmp.next = ListNode(int(addtion))
        return head.next