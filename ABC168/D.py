from collections import deque

N,M = map(int,input().split())
C = [[] for _ in range(N+1)]
for _ in range(M):
    tmp = list(map(int,input().split()))
    C[tmp[0]].append(tmp[1])
    C[tmp[1]].append(tmp[0])
d = [1000000000]*(N+1)
d[1] = 0
visited = [False]*(N+1)
q = deque()
q.append(1)

sirube = [0]*(N+1)
while q:
    node = q.popleft()
    for adj in C[node]:
        if visited[adj] == False:
            sirube[adj] = node
            q.append(adj)
            visited[adj] = True



print("Yes")
for i in range(2,N+1):
    print(sirube[i])

