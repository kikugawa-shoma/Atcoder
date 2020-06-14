N = int(input())
S = [input() for _ in range(N)]
S.sort()
h = {}
name = set(S)
for n in name:
    h[n] = 0

for s in S:
    h[s] += 1

max_h = max(h.values())
l = []
for s in set(S):
    if h[s] == max_h:
        l.append(s)

for i in sorted(l):
    print(i)

