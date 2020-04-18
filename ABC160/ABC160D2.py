from collections import deque
N, X, Y = map(int, input().split())
INF = N+1
q = deque()

def node_search(i):
    nodes = []
    if i < N and check[i+1] == 0:
        nodes.append(i+1)
    if i > 1 and check[i-1] == 0:
        nodes.append(i-1)
    if i == X and check[Y] == 0:
        nodes.append(Y)
    return nodes


cnt = [0]*N
for i in range(1, N):
    check = [0]*(N+1)
    dist = [INF] * (N + 1)
    dist[i] = 0
    q.append(i)
    d = 1
    while q:
        now_node = q.pop()
        check[now_node] = 1
        for next_node in node_search(now_node):
            dist[next_node] = min(dist[now_node]+1, dist[next_node])
            q.appendleft(next_node)


    for j in range(i+1, N+1):
        cnt[dist[j]] += 1

for i in range(1, N):
    print(cnt[i])


a = 0

