N = int(input())
P = list(map(float, input().split()))

#dp[i][j] = i枚目までのコインでj枚が表になる確率
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(N+1):
        if j == 0:
            dp[i][j] = (1-P[i-1])*dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j-1]*P[i-1] + dp[i-1][j]*(1-P[i-1])

ans = 0
for j in range(N+1):
    if j > (N-j):
        ans += dp[N][j]
print(ans)