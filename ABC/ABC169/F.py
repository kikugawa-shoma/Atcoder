import sys
sys.setrecursionlimit(100000)

N,S = map(int,input().split())
A = list(map(int,input().split()))
mod = 998244353
P = []

def BFS(now,i,pattern):
    if now == S:
        P.append(pattern)
    else:
        if i < N:
            if now + A[i] <= S:
                BFS(now+A[i],i+1,pattern+1)

            BFS(now,i+1,pattern)

BFS(0,0,0)

pow_2 = [1]*3010
for i in range(1,3010):
    pow_2[i] = (2*pow_2[i-1])%mod


ans = 0
n = len(P)
for i in range(n):
    l = P[i]
    ans += pow_2[N-l]
    ans %= mod
print(ans)

