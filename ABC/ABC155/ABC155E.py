N = input()

dp = [[0] * 2 for _ in range(len(N)+1)]

for i in range(1, len(N)+1):
    dp[i][0] = min(dp[i-1]) + int(N[i-1])
    if N[i-2]
    dp[i][1] = min(dp[i-1]) + 1 + (10-int(N[i-1]))

print(min(dp[-1]))