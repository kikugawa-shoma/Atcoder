N = int(input())
H = [int(h) for h in input().split()]

dp = [0]*(N+1)
dp[1] = abs(H[0]-H[1])

for n in range(2,N):
    dp[n] = min(dp[n-2] + abs(H[n] - H[n-2]), dp[n-1] + abs(H[n-1] - H[n]))

print(dp[N-1])