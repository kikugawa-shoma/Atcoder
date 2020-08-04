"""
9 5
-4 -3 -2 -1 0 1 2 3
"""

N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
Am = []
Ap = []
for a in A:
    if a < 0:
        Am.append(a)
    else:
        Ap.append(a)

mod = 10**9 + 7

ans = 1

if N == K:
    for a in A:
        ans *= a
        ans %= mod

elif A[-1] < 0:
    if K % 2 == 1:
        for i in range(K):
            ans *= Am[-1-i]
            ans %= mod
    else:
        for i in range(K):
            ans *= Am[i]
            ans %= mod

else:
    if K%2 == 1:
        ans *= Ap[-1]
        ans %= mod
        K -= 1
        del Ap[-1]
    Amd = []     
    Apd = []
    for i in range(len(Ap)//2):
        Apd.append(Ap[-1-(2*i)]*Ap[-1-(2*i+1)])
    for i in range(len(Am)//2):
        Amd.append(Am[2*i]*Am[2*i+1])
    Apd.append(-1)
    Amd.append(-1)
    
    ip = 0
    im = 0
    while K > 0:
        if Apd[ip] >= Amd[im]:
            ans *= Apd[ip]
            ip += 1
        else:
            ans *= Amd[im]
            im += 1
        ans %= mod
        K -= 2


ans %= mod
print(ans)


