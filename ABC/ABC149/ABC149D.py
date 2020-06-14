N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

dp = [[0] * 3 for _ in range(N + 1)]


def point(hand, n):
    n -= 1
    if hand == T[n]:
        return 0
    elif hand == "r" and T[n] == "p" or hand == "s" and T[n] == "r" or hand == "p" and T[n] == "s":
        return 0
    elif T[n] == "r":
        return P
    elif T[n] == "s":
        return R
    elif T[n] == "p":
        return S


for n in range(1, N + 1):
    if n <= K:
        dp[n][0] = point("r", n)
        dp[n][1] = point("s", n)
        dp[n][2] = point("p", n)
    else:
        dp[n][0] = max(dp[n-K][1], dp[n-K][2]) + point("r", n)
        dp[n][1] = max(dp[n-K][2], dp[n-K][0]) + point("s", n)
        dp[n][2] = max(dp[n-K][1], dp[n-K][0]) + point("p", n)

MaxPoint = 0
for k in range(K):
    MaxPoint += max(dp[N-k])

print(MaxPoint)


