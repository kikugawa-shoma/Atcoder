import heapq

N, M = map(int, input().split())
AB = (list(map(int, input().split())) for _ in range(N))

AB = sorted(AB, key=lambda x: x[0])
hq = []
ind = 0
ans = 0
for lim in range(1, M + 1):
    for i in range(ind, N):
        if AB[i][0] == lim:
            AB[i][0], AB[i][1] = -AB[i][1], AB[i][0]
            heapq.heappush(hq, AB[i])
            ind += 1
        else:
            break
    if hq:
        ans += -heapq.heappop(hq)[0]

print(ans)


