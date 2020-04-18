from collections import deque
from collections import Counter
N, M, K = map(int, input().split())
A = [0]*M
B = [0]*M
for i in range(M):
    A[i], B[i] = map(int, input().split())
C = [0]*K
D = [0]*K
for i in range(K):
    C[i], D[i] = map(int,input().split())

friend = {i: set([]) for i in range(1, N+1)}
brock = {i: set([]) for i in range(1, N+1)}
for i in range(M):
    friend[A[i]].add(B[i])
    friend[B[i]].add(A[i])
for i in range(K):
    brock[C[i]].add(D[i])
    brock[D[i]].add(C[i])

labels = [0] * (N+1)


def mark(n, label):
    if labels[n] != 0:
        return -1
    else:
        q = deque()
        q.append(n)
        labels[n] = label
        while q != deque():
            node = q.pop()
            labels[node] = label
            for i in friend[node]:
                if labels[i] == 0:
                    q.append(i)
        return label


label = 1
for n in range(1, N + 1):
    if mark(n, label) != -1:
        label += 1

group_size = Counter(labels)

res = [0] * N
for n in range(1, N + 1):
    tmp = 0
    for b in brock[n]:
        if labels[n] == labels[b]:
            tmp += 1
    res[n - 1] = group_size[labels[n]] - 1 - len(friend[n]) - tmp

print(*res)
