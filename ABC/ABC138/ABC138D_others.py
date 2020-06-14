import sys

input = sys.stdin.readline

n, q = map(int, input().split())
link = [[] for _ in range(n)]
for i in range(n - 1):
    tmp = list(map(int, input().split()))
    link[tmp[0] - 1].append(tmp[1] - 1)
    link[tmp[1] - 1].append(tmp[0] - 1)

from collections import defaultdict

d = defaultdict(int)
for i in range(q):
    tmp = list(map(int, input().split()))
    d[tmp[0] - 1] += tmp[1]

from collections import deque

ans = [0] * n
finish = {0}
Q = deque()
Q.append([0, 0])
while Q:
    node = Q.popleft()
    finish.add(node[0])

    val = node[1] + d[node[0]]
    ans[node[0]] += val

    for nxt in link[node[0]]:
        if nxt in finish:
            pass
        else:
            Q.append([nxt, val])

print(*ans)