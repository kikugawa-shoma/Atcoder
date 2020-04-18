
"""Python
import numpy as np

N, W = map(int, input().split())
WV = np.array([list(map(int, input().split())) for i in range(N)])

dp = np.zeros((N+1, W+1), dtype=np.int)
for n in range(1, N + 1):
    for w in range(1, W+1):
        if w >= WV[n-1][0]:
        # weight = max(w-WV[n-1][0], 0)
            dp[n][w] = max(dp[n-1][w-WV[n-1][0]] + WV[n-1][1], dp[n-1][w])
        else:
            dp[n][w] = dp[n-1][w]

print(dp[-1][-1])
"""

# pypy
N, W = map(int, input().split())
WV = [list(map(int, input().split())) for i in range(N)]

dp = [[0]*(W+1) for i in range(N+1)]
for n in range(1, N+1):
    for w in range(1, W+1):
        if w >= WV[n-1][0]:
            dp[n][w] = max(dp[n-1][w-WV[n-1][0]] + WV[n-1][1], dp[n-1][w])
        else:
            dp[n][w] = dp[n-1][w]
print(dp[-1][-1])


