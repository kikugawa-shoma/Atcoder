import sys
sys.setrecursionlimit(100000)

N = int(input())
A = list(map(int, input().split()))

start_plate = [0] * 3
for n in range(N):
    if A[n] > 0:
        start_plate[A[n] - 1] += 1

max_N = 301
memo = [[[0] * max_N for _ in range(max_N)] for __ in range(max_N)]


def dp(i1, i2, i3):
    if i1 == 0 and i2 == 0 and i3 == 0:
        return 0
    else:
        i_sum = i1 + i2 + i3
        tmp = N
        if i3-1 >= 0:
            if memo[i1][i2+1][i3-1] == 0:
                tmp += dp(i1, i2 + 1, i3 - 1) * i3
            else:
                tmp += memo[i1][i2+1][i3-1]*i3
        if i2-1 >= 0:
            if memo[i1+1][i2-1][i3] == 0:
                tmp += dp(i1 + 1, i2 - 1, i3) * i2
            else:
                tmp += memo[i1+1][i2-1][i3]*i2
        if i1-1 >= 0:
            if memo[i1-1][i2][i3] == 0:
                tmp += dp(i1 - 1, i2, i3) * i1
            else:
                tmp += memo[i1-1][i2][i3]*i1
        tmp /= i_sum
        memo[i1][i2][i3] = tmp
        return tmp


print(dp(start_plate[0], start_plate[1], start_plate[2]))