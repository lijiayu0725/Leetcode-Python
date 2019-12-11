# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len1 = self.lenth(headA)
        len2 = self.lenth(headB)
        longList = headA if len1 > len2 else headB
        shortList = headB if len1 > len2 else headA
        diff = abs(len1 - len2)
        while diff:
            diff -= 1
            longList = longList.next
        while longList is not shortList:
            longList = longList.next
            shortList = shortList.next
        return longList

    def lenth(self, head: ListNode) -> int:
        count = 0
        while head:
            head = head.next
            count += 1
        return count
