
mod = 10**9+7
N = int(input())


def mod_factorials(n, m):
    mod_factorials = [1] * (n + 1)
    for i in range(1, n+1):
        mod_factorials[i] = mod_factorials[i-1]*i
        mod_factorials[i] %= m
    return mod_factorials

# 1!,2!,3!,...,n! �εո� (mod m)
def mod_inv_factorials(n, m):
    mod_invs = [1] * (n + 1)
    invs = [1] * (n + 1)
    for i in range(2, n + 1):
        invs[i] = m - invs[m % i] * (m//i) % m

    for i in range(1, n+1):
        mod_invs[i] = invs[i]*mod_invs[i-1]
        mod_invs[i] %= m
    return mod_invs

if N == 1:
    print(0)
else:
    ans = 0
    pow8 = [1]*(N+1)
    pow2 = [1]*(N+1)
    mod_facts = mod_factorials(N,mod)
    mod_invs = mod_inv_factorials(N,mod)
    for i in range(1,N+1):
        pow8[i] = pow8[i-1]*8
        pow8[i] %= mod
        pow2[i] = pow2[i-1]*2
        pow2[i] %= mod

    for k in range(2,N+1):
        ans += mod_facts[N]*mod_invs[k]*mod_invs[N-k]*(pow2[k]-2)*pow8[N-k]
        ans %= mod
    ans %= mod 


    print(ans)


