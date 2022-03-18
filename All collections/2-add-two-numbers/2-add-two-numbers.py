# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []
        while l1 or l2:
            if l1:
                s1.insert(0,str(l1.val))
                l1 = l1.next
            if l2:
                s2.insert(0,str(l2.val))
                l2 = l2.next
        total = int(''.join(s1)) + int(''.join(s2))
        sumlist = list(map(int, str(total)))
        head = ListNode(0)
        res = head
        N = len(sumlist)
        for i in range(N):
            curr = ListNode(sumlist[N-i-1])
            head.next = curr
            head = curr
        return res.next