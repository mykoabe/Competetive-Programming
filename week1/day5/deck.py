class Deque:
    def __init__(self):
        self.items = []
    def remove_rear(self):
        return self.items.pop(0)
    def remove_front(self):
        return self.items.pop()
    def add_front(self, item):
        self.items.append(item)
    def add_rear(self, item):
        self.items.insert(0, item)
    def size(self):
        return len(self.items)
def palindromeChecker(palindrome):
    deque = Deque()
    for alpha in palindrome:
        deque.add_rear(alpha)
    while deque.size() > 2:
        front_item = deque.remove_front()
        rear_item = deque.remove_rear()
        if rear_item != front_item:
            return False
        return True
print(palindromeChecker("mom"))

