N, K = map(int, input().split())
H = [int(i) for i in input().split()]

H.sort()

if N-K >= 0:
    H[N-K:N] = [0]*K
else:
    H[:] = [0]*N
print(sum(H))




