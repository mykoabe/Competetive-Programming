class RecentCounter:
    
    def __init__(self):
        self.requests = []
        
    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < (t - 3000):
            self.requests.pop(0)
        return len(self.requests)
sol = RecentCounter()
sol.ping(1)
sol.ping(2)
sol.ping(100)
sol.ping(3002)
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)