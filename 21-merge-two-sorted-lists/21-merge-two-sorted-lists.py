# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        head = list1 if list1.val < list2.val else list2
        if head == list1:
            list1 = list1.next
        else:
            list2 = list2.next
        tail = head
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
            else:
                tail.next = list2
                tail = list2
                list2 = list2.next
        tail.next = list1 if list2 == None else list2
        return head
        