import numpy as np
N = int(input())

abc = np.array([list(map(int, input().split())) for i in range(N)])

dp = [[0]*3 for i in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = max(dp[i - 1][1] + abc[i - 1][1], dp[i - 1][2] + abc[i - 1][2])
    dp[i][1] = max(dp[i - 1][0] + abc[i - 1][0], dp[i - 1][2] + abc[i - 1][2])
    dp[i][2] = max(dp[i - 1][1] + abc[i - 1][1], dp[i - 1][0] + abc[i - 1][0])

print(max(dp[-1]))
