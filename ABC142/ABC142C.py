import heapq as hq

N = int(input())
A = [int(a) for a in input().split()]

h = []
for i in range(N):
    hq.heappush(h, (A[i], i+1))

for i in range(N):
    A[i] = hq.heappop(h)[1]

print(*A)
