N,S = map(int,input().split())
A = list(map(int,input().split()))
mod = 998244353

dp = [[0]*3005 for _ in range(3005)]
dp[0][0] = 1
for i in range(0,N):
    for s in range(0,S+1):
        if s-A[i] >= 0:
            dp[i+1][s] = dp[i][s]*2 + dp[i][s-A[i]]
        else:
            dp[i+1][s] = dp[i][s]*2
        dp[i+1][s] %= mod

print(dp[N][S])