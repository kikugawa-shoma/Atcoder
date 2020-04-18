N = int(input())
H = list(map(int, input().split()))
INF = 10000000000
dp = [INF] * N
dp[0] = 0

for i in range(N-1):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(H[i] - H[i + 1]))
    if i <= N - 3:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(H[i] - H[i + 2]))

print(dp[N - 1])
