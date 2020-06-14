N, K, M = map(int, input().split())
A = [int(i) for i in input().split()]

A_N = M*N - sum(A)
if A_N <= K:
    if A_N >=0:
        print(A_N)
    else:
        print(0)
else:
    print(-1)


