from collections import deque

N, X, Y = map(int, input().split())


def node_search(i):
    node_list = []
    if i != 1:
        node_list.append(i-1)
    if i != N:
        node_list.append(i+1)
    if i == X:
        node_list.append(Y)
    if i == Y:
        node_list.append(X)
    return node_list


def bfs(k):
    q = deque()
    dist = [N]*(N+1)
    q.append(k)
    check = [0]*(N+1)
    check[k] = 1
    dist[k] = 0
    while q:
        now_node = q.pop()
        check[now_node] = 1
        next_nodes = node_search(now_node)
        for node in next_nodes:
            if check[node] == 0:
                dist[node] = min(dist[now_node]+1, dist[node])
                q.appendleft(node)
    return dist


ans = [0]*N
for k in range(1, N+1):
    dist_list = bfs(k)
    for i in range(k+1, N+1):
        ans[dist_list[i]] += 1

for i in range(1, N):
    print(ans[i])



