K = int(input())
S = input()
N = len(S)

mod = 10**9+7

power25 = [1]*(K+1)
power26 = [1]*(K+1)

def mod_factorial(n, m):
    mod_factorials = [1] * (n + 1)
    for i in range(1, n+1):
        mod_factorials[i] = mod_factorials[i-1]*i
        mod_factorials[i] %= m
    return mod_factorials

# 1!,2!,3!,...,n! の逆元 (mod m)
def mod_inv_factorials2(n, m):
    mod_invs = [1] * (n + 1)
    invs = [1] * (n + 1)
    for i in range(2, n + 1):
        invs[i] = m - invs[m % i] * (m//i) % m

    for i in range(1, n+1):
        mod_invs[i] = invs[i]*mod_invs[i-1]
        mod_invs[i] %= m
    return mod_invs

factrials = mod_factorial(K+N,mod)
inv_factrials = mod_inv_factorials2(max(N,K+1),mod)

for i in range(1,K+1):
    power25[i] = (power25[i-1]*25)%mod
for i in range(1,K+1):
    power26[i] = (power26[i-1]*26)%mod

ans = 0
for i in range(K+1):
    rk = K-i
    ans += power25[rk]*factrials[rk+N-1]*inv_factrials[N-1]*inv_factrials[rk]*power26[i]
    ans %= mod

print(ans)

