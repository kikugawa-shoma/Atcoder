import heapq
class ErasableHeapq:
    def __init__(self):
        self.p = list()
        self.q = list()
        self.len = 0
 
    def insert(self, x):
        heapq.heappush(self.p, x)
        self.len += 1
        return
 
    def erase(self, x):
        heapq.heappush(self.q, x)
        self.len -= 1
        return
 
    def minimum(self):
        while self.q and self.p[0] == self.q[0]:
            heapq.heappop(self.p)
            heapq.heappop(self.q)
        return self.p[0]
 
    def __len__(self):
        return self.len
 
    def empty(self):
        return self.len == 0

q = ErasableHeapq()
q.insert(3)
q.insert(1)
q.insert(9)
q.insert(2)
print(q.minimum(),q.erase(1),q.minimum())