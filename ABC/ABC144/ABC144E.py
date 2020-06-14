'''
3 5
4 2 1
2 3 1
'''

N, K = map(int, input().split())
A = sorted([int(a) for a in input().split()])
F = sorted([int(f) for f in input().split()], reverse=True)
INF = 10**12+10

l = -1
r = INF
while r - l > 1:
    c = (l + r) // 2
    SUM_B = 0
    for i in range(N):
        SUM_B += max(0, A[i] - c//F[i])
    if SUM_B <= K:
        r = c
    else:
        l = c

print(r)


