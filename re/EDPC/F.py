S = input()
T = input()

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

for si in range(1, len(S) + 1):
    for ti in range(1, len(T) + 1):
        if S[si - 1] == T[ti - 1]:
            dp[si][ti] = dp[si - 1][ti - 1] + 1
        else:
            dp[si][ti] = max(dp[si][ti-1], dp[si-1][ti])

print(dp[len(S)][len(T)])

