import math
from collections import defaultdict

n = int(input())
A = list(map(int,input().split()))
mod = 10**9+7

divisor_primes = defaultdict(int)

def prime_factrizer(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

for a in A:
    factrized_a = prime_factrizer(a)
    for prime in factrized_a:
        divisor_primes[prime[0]] = max(divisor_primes[prime[0]],prime[1])

invs = [1] * (max(A) + 1)
for i in range(2, max(A) + 1):
    invs[i] = mod - invs[mod % i] * (mod//i) % mod

lcm = 1
for key in divisor_primes.keys():
    power = divisor_primes[key]
    div = 1
    for i in range(power):
        div *= key
        div %= mod
    lcm *= div

ans = 0

for a in A:
    ans += invs[a]
    ans %= mod
ans *= lcm
ans %= mod
print(ans)




