# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        while l1 != None:
            if l2 == None:
                if l1.val >= 10:
                    if l1.next == None:
                        l1.next = ListNode()
                    l1.next.val += l1.val // 10
                    l1.val %= 10
                l1 = l1.next
                continue
            l1.val += l2.val
            if l1.val >= 10:
                if l1.next == None:
                    l1.next = ListNode()
                l1.next.val += l1.val // 10
                l1.val %= 10
            l2 = l2.next
            if l1.next == None and l2 != None:
                l1.next = ListNode()
            l1 = l1.next
        return head
