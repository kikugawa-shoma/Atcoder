N, M = map(int, input().split())
broken_step = [0]*(N+1)
for i in range(M):
    broken_step[int(input())] = 1
broken_step.extend([0, 0, 0])

mod = 1000000007

dp = [0]*(N+5)
dp[0] = 1

for n in range(N):
    if broken_step[n+1] == 0:
        dp[n+1] += dp[n]*1
    else:
        dp[n+1] = 0
    if broken_step[n+2] == 0:
        dp[n+2] += dp[n]*1
    else:
        dp[n+2] = 0
print(dp[N]%mod)