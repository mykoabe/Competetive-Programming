# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        if head.next is None:
            return head
        curr = head
        while curr and curr.next:
            curr.val, curr.next.val = curr.next.val, curr.val
            curr = curr.next.next
        return head
            
            
            
        
        
