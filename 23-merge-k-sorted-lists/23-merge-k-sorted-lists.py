# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for head in lists:
            temp = head
            while temp:
                heapq.heappush(heap, temp.val)
                temp = temp.next
                
        head = ListNode(-1)
        sentinel = ListNode(-1, head)
        while heap:
            node = ListNode(heapq.heappop(heap))
            head.next = node
            head = head.next
        return sentinel.next.next
            
            
        