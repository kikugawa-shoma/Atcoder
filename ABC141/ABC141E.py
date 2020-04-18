"""
14
strangeoranges
"""

N = int(input())
S = input()

dp = [[0]*N for _ in range(N)]

for v in range(N):
    for h in range(N):
        if h == 0 or v == 0:
            if S[v] == S[h]:
                dp[v][h] = min(1, abs(v-h))
        elif S[v] == S[h]:
            dp[v][h] = min(dp[v-1][h-1] + 1, abs(v-h))

ans = 0
for i in range(N):
    tmp = max(dp[i])
    if tmp > ans:
        ans = tmp

print(ans)
