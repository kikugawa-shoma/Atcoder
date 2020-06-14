import bisect
S = input()
T = input()

dic = {chr(s): [] for s in range(ord("a"), ord("z") + 1)}
for i, s in enumerate(S):
    dic[s].append(i + 1)

out = 0
cnt = -1
V = [0] * len(T)
for i, t in enumerate(T):
    if dic[t]:
        """
        for l in dic[t]:
            if cnt < l:
                V[i] = l
                cnt = l
                break
        else:
            cnt = dic[t][0]
        """

        idx = bisect.bisect(dic[t], cnt)
        if idx == len(dic[t]):
            V[i] = dic[t][0]
            cnt = dic[t][0]
        else:
            V[i] = dic[t][idx]
            cnt = dic[t][idx]

    else:
        out = 1
        break
if out == 1:
    print(-1)
else:
    cnt = 0
    for i in range(len(V)-1):
        if V[i+1] <= V[i]:
            cnt += 1
    if cnt == 0:
        print(V[-1])
    elif V[-1] == len(S):
        print(len(S) * (cnt + 1))
    else:
        print(len(S) * cnt + V[-1])
a = 0