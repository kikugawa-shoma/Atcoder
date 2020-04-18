import numpy as np
N, K = map(int, input().split())
# H = np.array([int(h) for h in input().split()])
H = np.array(list(map(int, input().split())))

dp = np.zeros(N, dtype=int)
k = np.array([i for i in range(1, K+1)])

for n in range(1, N):
    start = max(n-K, 0)
    #if n < K:
    #   dp[n] = np.amin(dp[start] + np.abs(H[n]-H[start]))
    #else:
    #   dp[n] = np.min(dp[n - k] + np.abs(H[n] - H[n - k]))
    dp[n] = np.min(dp[start:n] + np.abs(H[n]-H[start:n]))

print(dp[N-1])

