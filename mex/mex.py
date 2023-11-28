from heapq import heappop,heappush,heapify
class Mex:    
    def __init__(self, arr=[], MAX=10**6) -> None:
        self.MAX = MAX + 5
        self.hist = [0] * (self.MAX+1)
        for a in arr:
            if a > self.MAX: continue
            self.hist[a] += 1
        self.q = []
        self.d = []
        for i in range(self.MAX+1):
            if self.hist[i] == 0:
                heappush(self.q, i)
    def get(self):
        while self.q and self.d and self.q[0]==self.d[0]:
            heappop(self.q)
            heappop(self.d)
        return self.q[0] if self.q else None
    def add(self, x):
        if x > self.MAX: return
        self.hist[x] += 1
        if self.hist[x] == 1:
            heappush(self.d, x)
    def remove(self, x):
        if x > self.MAX: return
        self.hist[x] -= 1
        if self.hist[x] == 0:
            heappush(self.q, x)

