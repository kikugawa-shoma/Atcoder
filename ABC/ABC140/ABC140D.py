N, K = map(int, input().split())
S = input()

nowLR = S[0]
group_num = 1
for i in range(1, N):
    if S[i] != nowLR:
        group_num += 1
        nowLR = S[i]

max_rev = int(group_num / 2)
if max_rev <= K:
    print(N-1)
else:
    print(N - (group_num - 2 * K))




a = 0



