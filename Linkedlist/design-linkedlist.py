class Linkedlist:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
    
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val
            
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val) 
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
          
        if index > self.size:
            return -1

        current = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            cur_index = 0
            while cur_index < index-1:
                cur = cur.next
                cur_index +=1
            cur.next = cur.next.next
        self.size -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
