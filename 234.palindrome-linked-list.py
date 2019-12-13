# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next
        head1 = head
        head2 = self.reverse(slow)

        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True

    def reverse(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        node = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return node

if __name__ == '__main__':
    solution = Solution()
    def constructListNode(nums):
        head = ListNode(0)
        tmp = head
        for n in nums:
            tmp.next = ListNode(n)
            tmp = tmp.next
        return head.next
    res = solution.isPalindrome(constructListNode([1,2,3]))
    print(res)

