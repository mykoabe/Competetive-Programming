# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0)
        start.next = head
        prev, cur = start, head
        while cur:
            if cur.next and cur.next.val < cur.val:
                while prev.next and prev.next.val < cur.next.val:
                    prev = prev.next
                temp = prev.next
                prev.next = cur.next
                cur.next = cur.next.next
                prev.next.next = temp
                prev = start
            else:
                cur = cur.next
        return start.next
                
            
        
