# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r = l1
        p1 = l1
        p2 = l2
        c = 0
        q = l2
        # b1 = l1
        # b2 = l2
        while p1 != None and p2 != None:
            s = 0
            s += p1.val + p2.val + c
            c = s // 10
            s = s % 10
            p1.val = s
            b1 = p1
            b2 = p2
            p1 = p1.next
            p2 = p2.next
        while p1 != None:
            s = 0
            s += p1.val + c
            c = s // 10
            s = s % 10
            b1 = p1
            p1.val = s
            p1 = p1.next
        while p2 != None:
            s = 0
            s += p2.val + c
            c = s // 10
            s = s % 10
            p2.val = s
            b1.next = p2
            b2 = p2
            b1 = b1.next
            p2 = p2.next
        if c != 0:
            new = ListNode(c)
            b1.next = new
        return r
        