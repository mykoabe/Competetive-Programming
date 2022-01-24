# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        mid = head
        while head.next != None:
            head = head.next
            if count % 2 != 0:
                mid = mid.next
            count += 1
        return mid
        