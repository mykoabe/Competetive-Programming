# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # this is done by converting the linkedlist to list with O(n) space and time
        res = []
        while head:
            res.append(head.val)
            head = head.next
        coll = []
        n = len(res)
        for i in range(n//2):
            coll.append(res[i] + res[n-1-i])
        return max(coll)
            
            
