#桁DP 最単純ver N以下の整数の個数
N = inout()

L = len(N)

dp = [[0]*2 for i in range(L+1)]
dp[0][0] = 0
dp[0][1] = 1
for keta in range(0, L):
    dp[keta+1][0] = dp[keta][0]*10 + dp[keta][1]*(int(N[keta]))
    dp[keta+1][1] = dp[keta][1]

print(dp[-1][0]+dp[-1][1])
#0も含むので(N+1)を出力で正解
a = 0
