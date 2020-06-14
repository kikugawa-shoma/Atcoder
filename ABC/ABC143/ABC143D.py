"""
7
218 786 704 233 645 728 389

4
3 4 2 1
"""
N = int(input())
L = sorted([int(l) for l in input().split()])
INF = 10**8
L.append(INF)
L.append(INF)

num = 0
for na in range(N-2):
    for nb in range(na+1, N - 1):
        r = N+1
        l = nb
        while r - l > 1:
            c = (l + r) // 2
            if L[c] < L[na] + L[nb]:
                l = c
            else:
                r = c
        num += l - nb

print(num)
