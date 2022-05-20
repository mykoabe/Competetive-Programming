# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        arr.sort()
        cur = dummy = ListNode(0)
        for elem in arr:
            cur.next = ListNode(elem)
            cur = cur.next
        return dummy.next
            
        
            
        
