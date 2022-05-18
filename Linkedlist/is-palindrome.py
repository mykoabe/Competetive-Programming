# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #optimized O(n) time and O(1) space
        reverse, fast = None, head
        while fast and fast.next:
            fast = fast.next.next
            head.next, reverse, head = reverse, head, head.next
        tail = head.next if fast else head
        
        is_pal = True
        while reverse:
            is_pal = is_pal and reverse.val == tail.val
            reverse.next, head, reverse = head, reverse, reverse.next
            tail = tail.next
                       
        return is_pal
        
        #linkedlist to list O(n) time and O(n) space complexity
#         if not head or not head.next:
#             return True
#         res = []
#         while head:
#             res.append(head.val)
#             head = head.next
#         return res == res[::-1]
        
        
