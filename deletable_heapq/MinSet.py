
m heapq import heappop,heappush,heapify
class MinSet:
    def __init__(self, arr=[]) -> None:
        self.q = arr
        heapify(self.q)
        self.d = []
    def add(self,x):
        heappush(self.q, x)
    def remove(self,x):
        heappush(self.d, x)
    def get_min(self):
        while self.q and self.d and self.q[0]==self.d[0]:
            heappop(self.q)
            heappop(self.d)
        return self.q[0] if self.q else None
    def pop_min(self):
        while self.q and self.d and self.q[0]==self.d[0]:
            heappop(self.q)
            heappop(self.d)
        return heappop(self.q)
    def is_empty(self):
        return self.get_min() is None

