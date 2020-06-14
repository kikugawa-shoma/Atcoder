import heapq

N = int(input())
V = [int(a) for a in input().split()]
h = []
for v in V:
    heapq.heappush(h, v)

for i in range(N-1):
    heapq.heappush(h, (heapq.heappop(h) + heapq.heappop(h)) / 2)

print(heapq.heappop(h))
