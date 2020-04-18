import heapq
q = []
N = int(input())
A = [int(input()) for _ in range(N)]
for i in range(N):
    heapq.heappush(q, -A[i])

MAX1 = -heapq.heappop(q)
MAX2 = -heapq.heappop(q)
for i in range(N):
    if A[i] == MAX1:
        print(MAX2)
    else:
        print(MAX1)


