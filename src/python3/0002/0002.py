# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        while l1 is not None:
            if l2 is None:
                if l1.val >= 10:
                    if l1.next is None:
                        l1.next = ListNode()
                    l1.next.val += l1.val // 10
                    l1.val %= 10
                l1 = l1.next
                continue
            l1.val += l2.val
            if l1.val >= 10:
                if l1.next is None:
                    l1.next = ListNode()
                l1.next.val += l1.val // 10
                l1.val %= 10
            l2 = l2.next
            if l1.next is None and l2 is not None:
                l1.next = ListNode()
            l1 = l1.next
        return head
