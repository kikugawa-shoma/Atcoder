N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
sortedAB = sorted(AB)
con = {i: [] for i in range(1, N+1)}
color = [0] * (N + 1)
for a, b in sortedAB:
    con[a].append(b)

for i in range(1, N + 1):
    now_c = 1
    for c in con[i]:
        if color[i] == now_c:
            now_c += 1
        color[c] = now_c
        now_c += 1

print(max(color))
for i in range(N-1):
    print(color[AB[i][1]])

a = 0
