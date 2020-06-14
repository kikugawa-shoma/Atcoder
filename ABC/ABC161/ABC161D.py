from collections import deque
K = int(input())

dp = [[0]*10 for _ in range(17)]
for i in range(10):
    dp[0][i] = 1

for keta in range(1, 17):
    for i in range(10):
        if 1 <= i and i <= 8:
            dp[keta][i] += dp[keta-1][i-1]+dp[keta-1][i]+dp[keta-1][i+1]
        if i == 0:
            dp[keta][i] += dp[keta-1][0]+dp[keta-1][1]
        if i == 9:
            dp[keta][i] += dp[keta-1][9]+dp[keta-1][8]
SUM = 0
for keta in range(17):
    SUM += sum(dp[keta][1:])
    if SUM >= K:
        break
SUM = 0
for i in range(keta):
    SUM += sum(dp[i][1:])

r = K-SUM
tmp_r = 0
for i in range(1, 10):
    tmp_r += dp[keta][i]
    if tmp_r >= r:
        tmp_r -= dp[keta][i]
        r -= tmp_r
        break
keta += 1
if keta == 1:
    print(i)
else:
    l=[i]
    rr = 0
    for k in range(keta-1, 0, -1):
        q = deque()
        if i == 0:
            q.append(0)
            q.append(1)
        elif i == 9:
            q.append(8)
            q.append(9)
        else:
            q.append(i-1)
            q.append(i)
            q.append(i+1)
        while q:
            num = q.popleft()
            rr += dp[k-1][num]
            if rr >= r:
                rr -= dp[k-1][num]
                l.append(num)
                i = num
                break
    keta = len(l)
    ans = 0
    for i in range(keta):
        ans += l[keta-i-1]*10**i
    print(ans)

