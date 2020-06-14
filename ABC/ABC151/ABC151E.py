""""
4 2
1 1 3 4
"""
N, K = map(int, input().split())
A = [int(i) for i in input().split()]
A.sort()

p = 10**9+7

fact = [1]*(N+1)
inv = [0]*(N+1)
inv[1] = 1
fact_inv = [1]*(N+1)
fact_inv = [1]*(N+1)
for i in range(2, N+1):
    fact[i] = (fact[i-1]*i) % p
    inv[i] = (-inv[p % i]*(p//i)) % p
    fact_inv[i] = (fact_inv[i-1]*inv[i] % p)


def cmb_mod(n, k, p):
    return (fact[n]*fact_inv[k]*fact_inv[n-k]) % p


max_sum = 0
min_sum = 0
for i in range(K-1, N):
    n_C_k = cmb_mod(i, K-1, p)
    max_sum += A[i] * n_C_k
    min_sum += A[N-i-1] * n_C_k
    max_sum = max_sum
    min_sum = min_sum

print((max_sum - min_sum) % p)