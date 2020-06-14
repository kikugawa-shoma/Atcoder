import heapq

N, M = map(int, input().split())
A = [-int(a) for a in input().split()]

H = []
for a in A:
    heapq.heappush(H, a)

for m in range(M):
    tmp = abs(heapq.heappop(H)) // 2
    heapq.heappush(H, -tmp)

SUM_A = 0
for h in H:
    SUM_A += int(h)
print(-SUM_A)
