S = input()
N = len(S)
S = list(S)
S.reverse()

dp = [[0]*13 for _ in range(N + 1)]
dp[0][0] = 1
mod = 10**9+7
pow10 = 1
for i in range(1, N + 1):
    if S[i-1] == "?":
        for j in range(13):
            for k in range(10):
                dp[i][(j + k*pow10) % 13] += dp[i-1][j]
    else:
        for j in range(13):
            dp[i][(j+int(S[i-1])*pow10) % 13] = dp[i-1][j]
    pow10 = (pow10 * 10) % 13
    for j in range(13):
        dp[i][j] %= mod

print(dp[N][5])
