from collections import defaultdict
import math

N = int(input())
d_ab = defaultdict(int)
d_ba = defaultdict(int)
mod = 1000000007
a0 = 0
b0 = 0
all0 = 0

for i in range(N):
    A,B = map(int,input().split())
    if A == 0 and B == 0:
        all0 += 1
    elif A == 0:
        a0 += 1
    elif B == 0:
        b0 += 1
    else:
        gcd = math.gcd(A,B)
        if (A < 0 and B > 0) or (A > 0 and B < 0):
            minus_f = True
        else:
            minus_f = False
        A //= gcd
        B //= gcd
        A = abs(A)
        B = abs(B)
        if minus_f:
            d_ab[(-A,B)] += 1
            d_ba[(B,A)] += 1
        else:
            d_ab[(A,B)] += 1
            d_ba[(-B,A)] += 1
        

ans = 1

#print(d_ab)
#print(d_ba)

pairs = list(map(list,d_ab.keys()))
visited = defaultdict(int)
#print(pairs)

for pair in pairs:
    ab = d_ab[tuple(pair)]
    ba = d_ba[tuple(pair)]
    r_pair = list(reversed(pair))
    if r_pair[0] > 0 and r_pair[1] > 0:
        r_pair[0] *= -1
    elif r_pair[1] < 0:
        r_pair[1] *= -1
    r_pair = tuple(r_pair)
    if ba != 0 and visited[tuple(pair)] == 0:
        visited[r_pair] = 1
        ans *= (pow(2,ab)+pow(2,ba)-1)
        ans %= mod
    if ba == 0 and visited[tuple(pair)] == 0:
        ans *= (pow(2,ab))
        ans %= mod
#    print(ans)

#print(visited)
ans *= (pow(2,a0)+pow(2,b0)-1)
ans %= mod

ans += all0 -1
ans %= mod

print(ans)