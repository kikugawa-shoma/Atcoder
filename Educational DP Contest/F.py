S = input()
T = input()

Ls = len(S)
Lt = len(T)

dp = [[0] * (Lt + 1) for _ in range(Ls + 1)]

for i in range(Ls):
    for j in range(Lt):
        if S[i] == T[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

match = []
now_row = Ls
now_column = Lt
while now_row > 0 and now_column > 0:
    if dp[now_row][now_column] == dp[now_row-1][now_column]:
        now_row -= 1
    elif dp[now_row][now_column] == dp[now_row][now_column-1]:
        now_column -= 1
    else:
        match.append(T[now_column-1])
        now_column -= 1
        now_row -= 1

match.reverse()
print("".join(match))
