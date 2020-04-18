"""
3 8
3 3
4 5
5 6
"""

N, W = map(int, input().split())
WV = [list(map(int, input().split())) for i in range(N)]

INF = 10**9+1000
SUM_V = sum([A[1] for A in WV])
dp = [[INF]*(SUM_V+1) for i in range(N+1)]
dp[0][0] = 0
for i in range(N+1):
    dp[i][0] = 0

for n in range(0, N):
    for v in range(0, SUM_V+1):
        if v >= WV[n][1]:
            dp[n+1][v] = min(dp[n][v-WV[n][1]] + WV[n][0], dp[n][v])
        else:
            dp[n+1][v] = dp[n][v]

for n in range(0, N+1):
    for v in range(0, SUM_V+1):
        if dp[n][v] <= W:
            dp[n][v] = -1

print(max([max([i for i, v in enumerate(dd) if v == -1]) for dd in dp]))

"""
# Answer
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()
 
def main():
    N,W=map(int,input().split())
    w,v=[0]*N,[0]*N
    for i in range(N):
        w[i],v[i]=map(int,input().split())
    dp=[[INF]*(10**5+1) for _ in range(N+1)]
    dp[0][0]=0
    ans=0
    for i in range(N):
        for value in range(10**5+1):
            dp[i+1][value]=min(dp[i+1][value],dp[i][value])
            if value>=v[i]:
                dp[i+1][value]=min(dp[i+1][value],dp[i][value-v[i]]+w[i])
            if dp[i+1][value]<=W:
                ans=max(ans,value)
    print(ans)
 
if __name__ == '__main__':
    main()
"""