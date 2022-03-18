# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev_head = ListNode()
        prev_head.next = head
        
        temp = prev_head
        while True:
            pointer = temp.next
            for _ in range(k):
                if pointer == None:
                    return prev_head.next
                pointer = pointer.next
            prev, curr = None, temp.next
            for i in range(k):
                curr.next, prev, curr = prev, curr, curr.next
            temp.next.next, temp.next, temp = curr, prev, temp.next
        return prev_head.next
        