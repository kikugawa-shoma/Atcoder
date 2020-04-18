from collections import deque

N, Q = map(int, input().split())
AB = {i: set() for i in range(1, N+1)}
for i in range(N - 1):
    tmpA, tmpB = map(int, input().split())
    AB[tmpA].add(tmpB)
    AB[tmpB].add(tmpA)
P = [0] * Q
X = [0] * Q
V = [0] * (N + 1)
for i in range(Q):
    P, X = map(int, input().split())
    V[P] += X

check = [0]*(N + 1)
q = deque()
q.append(1)
check[1] = 1
while q != deque():
    node = q.pop()
    for i in AB[node]:
        if check[i] == 1:
            continue
        V[i] += V[node]
        check[i] = 1
        q.appendleft(i)
print(*V[1:])




