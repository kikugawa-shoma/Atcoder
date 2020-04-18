H, W, K = map(int, input().split())
S = [0] * H
INF = 1000000

for h in range(H):
    S[h] = list(input())


def check(divH):
    MAP = [0] * H
    BitDivH = "".join(["{:0", str(H - 1), "b}"]).format(divH)
    cnt = 0
    for i, bit in enumerate(BitDivH):
        if bit == "1":
            cnt += 1
            MAP[i + 1] = cnt
        else:
            MAP[i + 1] = cnt
    after_tmp = [0] * (MAP[-1] + 1)
    cnt = 0
    out = 0
    for w in range(W):
        for h in range(H):
            after_tmp[MAP[h]] += int(S[h][w])
        for af in after_tmp:
            if af > K:
                out = 1
                break
        else:
            after_tmp = [0] * (MAP[-1] + 1)
    if out == 1:
        return INF
    else:
        for w in range(W):
            for h in range(H):
                after_tmp[MAP[h]] += int(S[h][w])
            for af in after_tmp:
                if af > K:
                    cnt += 1
                    after_tmp = [0] * (MAP[-1] + 1)
                    for h2 in range(H):
                        after_tmp[MAP[h2]] += int(S[h2][w])
                    break
        return cnt + MAP[-1]

MIN = INF
for i in range(2**(H - 1)):
    MIN = min(MIN, check(i))

print(MIN)
