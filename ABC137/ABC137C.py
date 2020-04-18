from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

DICS = defaultdict(int)

for s in S:
    d = [0] * 26
    for ch in s:
        d[ord(ch)-ord("a")] += 1
    DICS[tuple(d)] += 1
ans = 0
for key in DICS:
    if DICS[key] > 1:
        ans += DICS[key] * (DICS[key] - 1) // 2

print(ans)

