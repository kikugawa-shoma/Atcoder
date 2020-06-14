"""
5 20
10 14 19 34 33

5 21
10 14 19 34 33

5 3
10 14 19 34 33
"""

N, M = map(int, input().split())
A = sorted([int(a) for a in input().split()])
INF = (10 ** 5) * 2 + 10


# 和がmid以上の組み合わせ数を返す関数
def count(mid):
    ind = [0] * N
    I = 0
    for j in range(N - 1, -1, -1):
        for i in range(I, N):
            if A[i] + A[j] >= mid:
                I = i
                ind[j] = I
                break
        else:
            ind[j] = N
    return N ** 2 - sum(ind)


r = INF
l = 0

while r - l > 1:
    c = (r + l) // 2
    now_M = count(c)
    if now_M >= M:
        l = c
    elif now_M < M:
        r = c

print("{} {}".format(l, r))

# r以上の要素を数える
ind = [0] * N
I = N - 1
for j in range(N):
    for i in range(I, -1, -1):
        if A[i] + A[j] < l:
            I = i
            ind[j] = N-(I+1)
            break
        else:
            ind[j] = N

S = [0] * N
S[N-1] = A[N-1]
for i in range(N-2, -1, -1):
    S[i] = S[i+1] + A[i]

SUM = 0
for i in range(N):
    if ind[i] != 0:
        SUM += S[N - ind[i]] + ind[i] * A[i]

print(SUM)



