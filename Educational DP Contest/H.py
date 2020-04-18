H, W = map(int, input().split())
A = [input() for _ in range(H)]

dp = [[0]*W for _ in range(H)]

for h in range(H):
    for w in range(W):
        if h == 0 and w == 0:
            dp[h][w] = 1
        elif A[h][w] == "#":
            dp[h][w] = 0
        elif h == 0:
            dp[h][w] = dp[h][w-1]
        elif w == 0:
            dp[h][w] = dp[h-1][w]
        elif A[h][w] == ".":
            dp[h][w] = dp[h][w-1] + dp[h-1][w]

print(dp[H-1][W-1] % 1000000007)

