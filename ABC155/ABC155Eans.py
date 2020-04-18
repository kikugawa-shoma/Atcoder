n = input()

dp1 = [0] * (len(n) + 1)
dp2 = [1] * (len(n) + 1)

for i in range(1, len(n) + 1):
    m = int(n[i - 1])
    dp1[i] = min(dp1[i - 1] + m, dp2[i - 1] + 10 - m)
    dp2[i] = min(dp1[i - 1] + m + 1, dp2[i - 1] + 9 - m)

print(dp1[-1])
