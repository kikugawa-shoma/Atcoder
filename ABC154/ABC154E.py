N = int(input())
K = int(input())
strN = [int(n) for n in str(N)]
keta_N = len(strN)

dp = [[[0] * 2 for _ in range(5)] for _ in range(keta_N+1)]
dp[0][0][0] = 1
#dp[keta][k][smaller]

for keta in range(keta_N):
    Nb = strN[keta]
    for k in range(4):
        for smaller in range(2):
            if smaller == 1:
                dp[keta + 1][k][smaller] += dp[keta][k][smaller]
                dp[keta + 1][k + 1][smaller] += dp[keta][k][smaller] * 9
            if smaller == 0:
                if Nb == 0:
                    dp[keta + 1][k][smaller] += dp[keta][k][smaller]
                if Nb == 1:
                    dp[keta + 1][k][smaller + 1] += dp[keta][k][smaller]
                    dp[keta + 1][k+1][smaller] += dp[keta][k][smaller]
                if Nb >= 2:
                    dp[keta + 1][k][smaller + 1] += dp[keta][k][smaller]
                    dp[keta + 1][k+1][smaller + 1] += dp[keta][k][smaller] * (Nb - 1)
                    dp[keta+1][k+1][smaller] += dp[keta][k][smaller]

print(dp[keta_N][K][0] + dp[keta_N][K][1])

"""answer example
digits = [int(c) for c in input()]
n = len(digits)
m = int(input())
 
dp = [[[0 for _ in range(2)] for _ in range(m + 2)] for _ in range(n + 1)]
dp[0][0][0] = 1
 
for i, digit in enumerate(digits):
    for j in range(m + 1):
        for k in range(2):
            for d in range(10 if k else digit + 1):
                dp[i + 1][j + (d > 0)][k or (d < digit)] += dp[i][j][k]
 
print(sum(dp[n][m]))
"""


