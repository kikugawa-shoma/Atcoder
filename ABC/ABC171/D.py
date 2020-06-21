from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))
Q = int(input())
B = [0]*Q
C = [0]*Q
for i in range(Q):
    B[i],C[i] = map(int,input().split())

d = defaultdict(int)

for a in A:
    d[a] += 1
S = sum(A)

for q in range(Q):
    b = B[q]
    c = C[q]
    if d[b]==0:
        print(S)
    else:
        S -= d[b]*b
        S += c*d[b]
        d[c] += d[b]
        d[b] = 0
        print(S)









