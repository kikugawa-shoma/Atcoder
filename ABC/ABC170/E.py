import heapq
import sys
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

if __name__ == "__main__":
    input = sys.stdin.readline
    en_num = 2*10**5+1
    N,Q = map(int,input().split())
    childs_en = [0]*(N+1)
    en = [ErasableHeapq() for _ in range(en_num)]
    strongests = ErasableHeapq()
    childs_rate = [0]*(N+1)

    for i in range(1,N+1):
        A,B = map(int,input().split())
        childs_en[i] = B
        en[B].insert(-A)
        childs_rate[i] = A

    for i in range(1,en_num):
        if not en[i].empty():
            strongests.insert(-en[i].minimum())


    C = [0]*(Q)
    D = [0]*(Q)
    for q in range(Q):
        C[q],D[q] = map(int,input().split())

    ans = [0]*Q
    for q in range(Q):
        child = C[q]
        next_en = D[q]
        rate = childs_rate[child]
        pre_en = childs_en[child]

        strongests.erase(-en[pre_en].minimum())
        en[pre_en].erase(-rate)
        if not en[pre_en].empty():
            strongests.insert(-en[pre_en].minimum())

        if not en[next_en].empty():
            strongests.erase(-en[next_en].minimum())
        en[next_en].insert(-rate)
        strongests.insert(-en[next_en].minimum())

        childs_en[child] = next_en

        ans[q] = strongests.minimum()

    for a in ans:
        print(a)

