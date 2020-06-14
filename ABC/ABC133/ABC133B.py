import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(0, N - 1):
    for j in range(i + 1, N):
        dist = 0
        f = 0
        for d in range(D):
            dist += (X[i][d] - X[j][d])**2
        root = int(math.sqrt(dist))
        for r in range(root-2, root+3):
            if r**2 == dist:
                f = 1
        if f == 1:
            ans += 1

print(ans)