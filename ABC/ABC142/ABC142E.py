N, M = map(int, input().split())
A = [0] * M
B = [0] * M
C = [0] * M
for m in range(M):
    A[m], B[m] = map(int, input().split())
    C[m] = [int(cm) for cm in input().split()]

INF = 100000000
dp = [[INF] * 2**N for _ in range(M + 1)]
dp[0][0] = 0


def Set2Bit(st):
    bt = ["0"]*N
    for i in st:
        bt[i-1] = "1"
    return bt


for m in range(0, M):
    key = Set2Bit(C[m])
    key_bit = int("".join(key), 2)
    for bit in range(2**N):
        pre_bit = next_bit = bit
        dp[m+1][next_bit] = dp[m][pre_bit]
    for bit in range(2**N):
        pre_bit = bit
        next_bit = pre_bit | key_bit
        dp[m+1][next_bit] = min(dp[m+1][next_bit], dp[m][next_bit], dp[m][pre_bit] + A[m])

if dp[-1][-1] == INF:
    print(-1)
else:
    print(dp[-1][-1])
