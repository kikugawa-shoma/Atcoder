from collections import defaultdict

H,W,M = map(int,input().split())
bomb = [[0,0] for _ in range(M)]
bomb_d = defaultdict(int)

for i in range(M):
    bomb[i] = list(map(int,input().split()))
    bomb[i][0] -= 1
    bomb[i][1] -= 1
    bomb_d[tuple(bomb[i])] = 1


dh = [0]*H
dw = [0]*W

for i in range(M):
    dh[bomb[i][0]] += 1
    dw[bomb[i][1]] += 1

Maxh = max(dh)
Maxw = max(dw)

h_p = []
w_p = []

for i in range(H):
    if dh[i] == Maxh:
        h_p.append(i)
for i in range(W):
    if dw[i] == Maxw:
        w_p.append(i)

f = 0
for h in h_p:
    for w in w_p:
        if bomb_d[(h,w)] != 1:
            f = 1
            break
    else:
        continue
    break

if f == 0:
    print(Maxh+Maxw-1)
else:
    print(Maxh+Maxw)











