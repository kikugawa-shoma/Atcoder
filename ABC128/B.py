from collections import defaultdict
N = int(input())
S = [0]*N
P = [[0]*2 for _ in range(N)]
d = defaultdict(lambda :[])
for i in range(N):
    tmp = input().split()
    d[tmp[0]].append([int(tmp[1]),i+1])

key = sorted(dict(d))
for k in key:
    tmp = sorted(d[k],reverse = True)
    for t in tmp:
        print(t[1])

