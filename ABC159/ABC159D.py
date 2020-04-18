from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
D = defaultdict(int)
for a in A:
    D[a] += 1

memo = defaultdict(lambda: -1)
conv_D = defaultdict(int)
SUM = 0
for d in D:
    conv_D[d] = D[d] * (D[d] - 1) // 2
    SUM += conv_D[d]

for i in range(N):
    if memo[A[i]] == -1:
        tmp = SUM - conv_D[A[i]] + (D[A[i]] - 1)*(D[A[i]] - 2)//2
        print(tmp)
        memo[A[i]] = tmp
    else:
        print(memo[A[i]])


a = 0
