import sys
import math
K=int(sys.stdin.readline()[:-1])
ans=0
for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            ans += math.gcd(k,math.gcd(i,j))

print(ans)
